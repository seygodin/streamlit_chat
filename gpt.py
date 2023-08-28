from langchain.chat_models import ChatOpenAI
import streamlit as st



your_api_key = st.text_input(label="YOUR OPENAI API KEY")

if your_api_key:
    chatbot = ChatOpenAI(openai_api_key=your_api_key, max_tokens=1000)

query = st.text_input(label="User Query")

if query:
    response = chatbot.predict(query)

    st.text_area("Answer", response, height=600)