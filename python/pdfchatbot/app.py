import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI

# ── Page config ──────────────────────────────────────────────
st.set_page_config(page_title="PDF Chatbot", page_icon="📄", layout="centered")
st.title("📄 Chat with your PDF")
st.caption("Upload any PDF and ask questions — powered by RAG + LLM")

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...")
    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown("1. PDF gets split into chunks")
    st.markdown("2. Chunks converted to embeddings")
    st.markdown("3. Your question searches the chunks")
    st.markdown("4. LLM answers using relevant chunks")

# ── Session state ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

# ── PDF Upload & Processing ───────────────────────────────────
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file and api_key and not st.session_state.pdf_loaded:
    with st.spinner("Processing your PDF..."):

        # Step 1: Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Step 2: Load PDF
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        # Step 3: Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(documents)

        # Step 4: Embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Step 5: Vector store
        vectorstore = Chroma.from_documents(chunks, embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # Step 6: LLM + Prompt
        llm = ChatOpenAI(
            model="gpt-4o-mini",  # better + cheap
            openai_api_key=api_key,
            temperature=0
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful assistant that answers questions
based on the provided document context. Be concise and accurate.
If the answer is not in the context, say so honestly.

Context:
{context}"""),
            ("human", "{input}")
        ])

        parser = StrOutputParser()

        # ✅ RAG pipeline (LangChain v1 style)
        def rag_pipeline(question):
            docs = retriever.invoke(question)

            context = "\n\n".join([doc.page_content for doc in docs])

            chain = prompt | llm | parser
            answer = chain.invoke({
                "context": context,
                "input": question
            })

            return answer, docs

        st.session_state.rag_chain = rag_pipeline
        st.session_state.pdf_loaded = True

        os.unlink(tmp_path)

    st.success(f"✅ Done! {len(chunks)} chunks created. Ask your questions below.")

elif uploaded_file and not api_key:
    st.warning("Enter your OpenAI API key in the sidebar first.")

# ── Chat UI ───────────────────────────────────────────────────
if st.session_state.pdf_loaded:

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if question := st.chat_input("Ask anything about your PDF..."):
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):
                answer, sources = st.session_state.rag_chain(question)

            st.write(answer)

            with st.expander("📚 Sources used"):
                for i, doc in enumerate(sources):
                    page = doc.metadata.get("page", 0)
                    st.markdown(f"**Chunk {i+1} — Page {page+1}:**")
                    st.caption(doc.page_content[:300] + "...")

        st.session_state.messages.append({"role": "assistant", "content": answer})

elif not uploaded_file:
    st.info("👆 Upload a PDF above to get started.")