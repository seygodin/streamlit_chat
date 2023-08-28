from langchain.chat_models import ChatOpenAI
import streamlit as st
import openai
from pyparsing import empty

def check_gpt_api_response(your_api):
    try:
        openai.api_key = your_api
        # 간단한 요청을 API에 보냅니다.
        response = openai.Completion.create(
          engine="davinci",
          prompt="Hello, GPT-4.",
          max_tokens=5
        )
        
        # API 호출이 성공적으로 완료되면, 응답이 존재한다는 것을 확인할 수 있습니다.
        if response:
            return True, "API에서 응답을 받았습니다."
        else:
            return False, "API에서 응답을 받지 못했습니다."

    except Exception as e:
        return False, f"API 요청 중 오류 발생: {str(e)}"

st.set_page_config(page_title="Serial GPT",layout="wide")


empty11, cont1, empty21 = st.columns([0.3, 1.0, 0.3])
empty12, but1, empty22 = st.columns([1.2, 0.1, 0.3])
empty13, cont2, empty23 = st.columns([0.3, 1.0, 0.3])

#First Row
with empty11:
    empty()
with cont1:
    st.title("Serial GPT Question and Answering")
    your_api_key = st.text_input(label="YOUR OPENAI API KEY")
    
    
    if your_api_key:
        if check_gpt_api_response(your_api_key)[0]:
            query_develop_model = ChatOpenAI(openai_api_key=your_api_key)
            query_check_model = ChatOpenAI(openai_api_key=your_api_key)
            query_model = ChatOpenAI(openai_api_key=your_api_key) 
            st.text("[API check]: Valid API.")
        
        else:
            st.text("[Warning]: Invalid API. Please check your api key from openai.com and try again")
        
    query = st.text_input(label="User Query")    
with empty21:
    empty()

#Second Row    
with empty12:
    empty()
with but1:
    run_buttton = st.button("Run AI")
with empty22:
    empty()    
    
#Third Row
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
