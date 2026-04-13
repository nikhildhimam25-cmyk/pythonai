import streamlit as st
if "quiz" not in st.session_state:
  st.session_state.quiz = []
if "ans" not in st.session_state:
    st.session_state.ans = []
if "check" not in st.session_state:
    st.session_state.check = []
  
st.set_page_config(page_title="Quiz App", page_icon="🧠")
st.title("WELCOME TO QUIZ APP ")
with st.sidebar:
    select=st.radio(label="menu",options=["ADD QUESTIONS","LIST","UPDATE","DELETE","PLAY"])
if select=="ADD QUESTIONS":
 st.session_state.quizz=[]
 st.session_state.anss=[]
 q=st.text_input("enter question..").strip()
 q1=st.text_input('1..enter option..').strip()
 q2=st.text_input('2..enter option..').strip()
 q3=st.text_input('3..enter option..').strip()
 q4=st.text_input('4..enter option..').strip()
 q5=st.selectbox(options=[q1,q2,q3,q4],label="CORRECT OPTION",placeholder="select correct option")
 if st.button(label="ADD",key="add"):
  if q and q1 and q2 and q3 and q4:
    st.session_state.quizz.append(q)
    st.session_state.quizz.append(q1)
    st.session_state.quizz.append(q2)
    st.session_state.quizz.append(q3)
    st.session_state.quizz.append(q4)
    st.session_state.quiz.append(st.session_state.quizz)
    st.session_state.anss.append(q5)
    st.session_state.ans.append(st.session_state.anss)
    st.success("QUESTION ADDED SUCESSFULLY")
if  select=="LIST":
 if not st.session_state.quiz:
   st.write("NO QUESTIONS SAVED YET")
 else:
   for i,j in enumerate(st.session_state.quiz[0:len(st.session_state.quiz)]):
    st.write("Q..",i+1,j[0],"?")
    st.write("1.",j[1])
    st.write("2.",j[2])
    st.write("3.",j[3])
    st.write("4.",j[4])
if select=="UPDATE":
  st.subheader("UPDATE QUIZ")
  if not  st.session_state.quiz:
    st.write("NO QUESTIONS YET")
  else:
    opt=["QUESTION","OPTION 1","OPTION 2","OPTION 3","OPTION 4"]
    a=st.number_input(min_value=1,max_value=len(st.session_state.quiz),label="enter question number")
    option=st.selectbox(label="select what to change",options=opt)
    a3=st.text_input("enter new option/question ")
    if st.button("UPDATE",key="update"):
      if option==opt[0]:
       st.session_state.quiz[a-1][0]=a3
      if option==opt[1]:
       st.session_state.quiz[a-1][1]=a3
      if option==opt[2]:
       st.session_state.quiz[a-1][2]=a3
      if option==opt[3]:
       st.session_state.quiz[a-1][3]=a3
      if option==opt[4]:
       st.session_state.quiz[a-1][4]=a3
      st.success("UPDATED SUCESSFULLY")
if select=="DELETE":
  st.subheader("DELETE QUIZ")
  if not  st.session_state.quiz:
    st.write("NO QUESTIONS YET")
  else:
   a=st.number_input(min_value=1,max_value=len(st.session_state.quiz),label="enter question number")
   if st.button(label="DELETE OUESTION",key="DELETE"):
     st.session_state.quiz.pop(a-1)
     st.success("QUESTION DELETED SUCESSFULLY")
if select=="PLAY":
  st.subheader("PLAY QUIZ")
  if not  st.session_state.quiz:
    st.write("ADD SOME QUESTIONS TO PLAY ")
  else:
    st.session_state.check = []   
    for i,j in enumerate(st.session_state.quiz):
      st.write(st.session_state.quiz[i][0])
      a = st.radio(
          label="",
          options=st.session_state.quiz[i][1:5],
          key=f"q{i}"
      )
      st.session_state.check.append(a)

    if st.button(label="SUBMIT", key="play"):
      score = 0
      for i in range(len(st.session_state.ans)):
        if st.session_state.check[i] == st.session_state.ans[i][0]:
          score += 1

      st.success("QUIZ COMPLETED")
      st.write("YOUR SCORE IS:", score)
      




