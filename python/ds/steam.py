

+--
import streamlit as st 
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Home Page', page_icon='🏠')
st.title('Nikhil Dhiman | Portfolio')
st.image("https://cdn.magicdecor.in/com/2023/10/26161313/Marvelous-Hulk-Hues-1.jpg")
st.subheader('About Me')
st.write('Hello, my name is Nikhil. I am from Himachal Pradesh. I am currently pursuing a BScfrom Indira Gandhi National Open University. Alongside my academics, I am learning Python for data analysis, automation, and real-world applications.')
st.write('I believe Python will help me build a strong foundation in coding and problem-solving and open up opportunities in the field of science and technology')
with st.form(key='key'):
 col1,clo=st.columns(2)
with col1:
  name=st.text_input("Name",max_chars=27,placeholder="enter your good name")
  password=st.text_input('password',type='password')
  gender=st.radio('gender',options=["male","female",'other'],horizontal=True)
  with clo:
    age=st.number_input("age",max_value=99)
    state=st.selectbox('state',options=['hp','jk','pb','ch'])
    hobbies=st.multiselect('hobbies',options=["singing",'eating','dancing','killing'])

with st.sidebar:
  menu=st.radio('menu',options=['home','contact','blog'])
  if menu=='Home':
    st.title("Home Page")
  elif menu=='Contact':
    st.title("Contact Page")
  else:
    st.title("Blog")
menu= option_menu(menu_title='', options=['Home','Contact','Blog','About'], icons=['house-fill','phone-fill','book-fill','info-square-fill'], orientation='horizontal')

