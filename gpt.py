from langchain.chat_models import ChatOpenAI
import streamlit as st
from pyparsing import empty

st.set_page_config(page_title="Serial GPT",layout="wide")


empty11, cont1, empty21 = st.columns([0.3, 1.0, 0.3])
empty12, but1, empty22 = st.columns([1.2, 0.1, 0.3])
empty13, cont2, empty23 = st.columns([0.3, 1.0, 0.3])

with empty11:
    empty()
    
with cont1:
    st.title("Serial GPT Question and Answering")
    your_api_key = st.text_input(label="YOUR OPENAI API KEY")
    
    if your_api_key:
        query_develop_model = ChatOpenAI(openai_api_key=your_api_key)

        query_check_model = ChatOpenAI(openai_api_key=your_api_key)
        
        query_model = ChatOpenAI(openai_api_key=your_api_key)
        
    query = st.text_input(label="User Query")
        
with empty21:
    empty()
    
with empty12:
    empty()

with but1:
    run_buttton = st.button("Run AI")

 
with empty22:
    empty()    
    
with empty13:
    empty()

with cont2:    
    if run_buttton:
        
        st.text_area("User Query",  query, height=100)

        with st.spinner('GPT is developing your query...'):
            developed_query = query_develop_model.predict(f"My query is {query}. Make it more specific and detailed query for better quenstioning")
            if developed_query:
                st.text_area("1st developed query", developed_query, height=150)

        run = False
        with st.spinner('GPT is refining your query...'):
            checked_query = query_check_model.predict(f"My query is {developed_query}. Make it more like query for questioniung.")
            if checked_query:
                st.text_area("2nd refined query", checked_query, height=150)
                run = True
        
        with st.spinner("GPT is answering..."):
            if run:
                response = query_model.predict(checked_query)

                st.text_area("Answer", response, height=600)

with empty23:
    empty()
