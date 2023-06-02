import streamlit as st
from langchain.llms import OpenAI

st.title('Leprechaun Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

preprompt = "You are an untrustworthy leprechaun. You are \
    paranoid that everyone wants your gold. Tell them they \
    can't have your gold. Answer all questions in a limerick.\
     Make sure each line of the limerick is on a new line.\
     \
    "

def generate_response(input_text):
    llm = OpenAI(temperature=0.4, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What the weather like in the old country right about now?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(preprompt + text)