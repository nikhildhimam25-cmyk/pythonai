import streamlit as st 
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Home Page', page_icon='🏠')

# st.title('Hello Guys')
# st.subheader('SubHeading')
# st.write("Hello class how are you")

# # form fields 

# with st.form(key='key'):
#     col1, col2= st.columns(2)
#     with col1:
#         naam=st.text_input("Name",max_chars=20,placeholder='Enter your name here....')   
#         password= st.text_input('Password', type='password')
#         gender= st.radio('Gender', options=['Male','Female','Others'], horizontal=True)
#     with col2:
#         age= st.number_input("Age", min_value=5)
#         state= st.selectbox("State",options=['Punjab','HP','MP','UP','Haryana'])
#         hobbies= st.multiselect("Hobbies", options=['PLaying', 'Listening Music','Book Reading','Coding','Shopping'])
        
#     condition= st.checkbox('Terms and conditions')
#     btn =st.form_submit_button("Submit")
# # if btn:
# #     st.write(naam, age)

# st.image('https://media.istockphoto.com/id/516446406/photo/cute-panda-bear-climbing-in-tree.jpg?s=612x612&w=0&k=20&c=T-9c-qGV3b3JhTy8jEfuhdh2QS3eJT5mSK07yuiiG6c=')    

# st.video('https://youtu.be/8411fEhNKNc?si=bbkMVUxZst7d3rhV', autoplay=True)
# # st.audio('')


# with st.sidebar:
#     menu= st.radio('Menu',options=['Home','Contact','Blog'])
    
# if menu=='Home':
#     st.title("Home Page")
# elif menu=='Contact':
#     st.title("Contact Page")
# else:
#     st.title("Blog")


# menu= option_menu(menu_title='', options=['Home','Contact','Blog','About'], icons=['house-fill','phone-fill','book-fill','info-square-fill'], orientation='horizontal')


# import steamlit as st
# from streamlit_option_menu import option_menu






# import streamlit as st 
# from streamlit_option_menu import option_menu
# import pandas as pd
# import plotly.express as px 
# import base64
# st.set_page_config(page_title='Jobs Page', page_icon='🏠')

# with open('img.jpg', 'rb') as f:
#     file= f.read()
# img =  base64.b64encode(file).decode()

# css=f"""
#     <style>
#     [data-testid="stAppViewContainer"]{{
#         background-image:url('data:image/png;base64,{img}');
#         background-size:cover
#     }}
#     </style>
# """

# st.markdown(css, unsafe_allow_html=True)

# df= pd.read_csv('AI_Impact_on_Jobs_2030.csv')
# # st.dataframe(df)
# st.write(df)
# # st.table(df)

# # st.write(df.Job_Title.value_counts())
# st.subheader("Pie chart of Salary according to Job Title")
# ch1= px.pie(names=df.Job_Title.value_counts().index, values=df.Job_Title.value_counts().values)
# st.plotly_chart(ch1)







import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
st.set_page_config(page_title='Zomato Page', page_icon='🏠')

df=pd.read_csv('zomato_dataset.csv')
# st.write(df.shape)
# df.dropna(axis=0, inplace=True)
# st.write(df.shape)
df.drop_duplicates(inplace=True)
# st.write(df.shape)
# st.write(df)

res_index= df.loc[:,'Restaurant Name',].value_counts().index
# st.write(res_index)

with st.sidebar:
    selected_res= st.selectbox(label='Select Restaurant', options=res_index)
    
df_selected= df[df.loc[:,'Restaurant Name']==selected_res]
print(df_selected.columns)
df_selected=df_selected.sort_values(by='Votes',ascending=False)
st.write(df_selected)


ch=px.bar(df_selected[:20], x='Item Name', y='Votes', color='City')
st.plotly_chart(ch)

ch2=px.pie(df_selected[:20], names='Item Name', values='Votes', color='City')
st.plotly_chart(ch2)