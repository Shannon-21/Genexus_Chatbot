# importing libraries
import streamlit as st
import pandas as pd
import os


# setting of frontend
st.title('GxBot')

# data for RAG
cwd = os.getcwd()
csv_file_path = os.path.join(cwd, 'data', 'genexus_wiki.csv')
df_menu = pd.read_csv(csv_file_path)

# store messages in memory
if 'messages' not in st.session_state:
    st.session_state.messages = []

# mark the turn of the role
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# display on prompt
prompt = st.chat_input('Pass Your Prompt here')

if prompt:
    # add user message
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})
    # get response from model and store it
    response =  df_menu['Title'].loc[0] #'hello'
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append(
        {'role':'assistant', 'content':response})