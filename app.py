# these are the libraries
import os
import PIL
import google.generativeai as genai
import streamlit as st
os.environ['GEMINI_IMAGE_API_KEY']='enter your api'
genai.configure(api_key=os.environ['GEMINI_IMAGE_API_KEY'])
def get_gemini_response(input_text,image):
  model=genai.GenerativeModel('GEMINI 1.5 PRO')
  if input_text !=" ":
    response = model.generate_content(['input_text image'])
  else:
    response = model.generate_content('image')
  return response.text
st.set_page_config(page_title='Uncover Insights Hidden in Your Photos')
st.header('Uncover Insights Hidden in Your Photos')
st.markdown("<h3 style='font-size: 23px;'>Developed by : Syed Musharaf </h3>", unsafe_allow_html=True)
input_text=st.text_input('Enter your text',key='input')
upload_file=st.file_uploader('Upload your image for Analyse',type=['png','jpg','jpeg'])
image = None
if upload_file is not None:
  image=image.open(upload_file)
  st.image(image,caption='Your uploaded image',use_column_width=True)
submit = st.button('Explain breif about the image')
if submit:
  if image is not None:
    response = get_gemini_response(input_text,image)
    st.header('The response is :')
    st.write(response)
  else:
    st.write('Please upload your image for analysing and response process')


