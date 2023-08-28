from langchain.chat_models import ChatOpenAI
import streamlit as st



your_api_key = st.text_input(label="YOUR OPENAI API KEY")

if your_api_key:
    query_develop_model = ChatOpenAI(openai_api_key=your_api_key)

    query_check_model = ChatOpenAI(openai_api_key=your_api_key)
    
    query_model = ChatOpenAI(openai_api_key=your_api_key)
    

    #query from user
    query = st.text_input(label="User Query")
    run_buttton = st.button("Run AI")
    if run_buttton:
        st.text_area("User Query",  query, height=100)


        developed_query = query_develop_model.predict(f"My query is {query}. Make it more specific and detailed query for better quenstioning")
        if developed_query:
            st.text_area("1st developed query", developed_query, height=150)

        run = False
        checked_query = query_check_model.predict(f"My query is {developed_query}. Make it more like query for questioniung.")
        if checked_query:
            st.text_area("2nd refined query", checked_query, height=150)
            run = True
            
        if run:
            response = query_model.predict(checked_query)

            st.text_area("Answer", response, height=600)
