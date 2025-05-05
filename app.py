import streamlit as st
from client import connection_start

connection = connection_start()



prompt = st.chat_input()

 
if prompt:
    st.chat_message("user").write(prompt)
    
    response = connection.get_chat_sync(prompt)
    
    st.chat_message("assistant").write(response)



