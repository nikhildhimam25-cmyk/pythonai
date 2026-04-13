import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64 
import seaborn as sns
import matplotlib.pyplot as plt 
st.set_page_config(page_title='home',page_icon='🏠')

with open('moon.webp','rb') as f:
    file=f.read()
img =  base64.b64encode(file).decode()

css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url('data:image/png;base64,{img}');
        background-size:cover
    }}
    </style>"""
st.markdown(css, unsafe_allow_html=True)
df=pd.read_csv("zomato_dataset.csv")
df.drop_duplicates(inplace=True)
var=df.loc[:,"Restaurant Name"].value_counts().index
with st.sidebar:
    select_df=st.selectbox(label="select restaurant",options=var)
         
df_sel=df[df.loc[:,"Restaurant Name"]==select_df]
select_df = df.copy()
def_sel=select_df.sort_values(by="Votes",ascending=False)
st.write(df_sel)

char=px.pie(df_sel[:20],names="Item Name",values="Votes",title="TOP 20 RESTAURENTS")
st.plotly_chart(char)


ch=px.bar(df_sel[:20], x='Item Name', y='Votes', color='City')
st.plotly_chart(ch)

# val=df[df["Best Seller"].isin(['BESTSELLER',"CHEF'S SPECIAL","MUST TRY"])].head(50)
# st.write(val)
# fig, ax = plt.subplots()
# sns.barplot(val, x='Best Seller', y='Votes',hue="Votes", ax=ax)
# st.pyplot(fig)