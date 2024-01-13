import openai
import streamlit as st

# 제목
c30, c32 = st.columns([0.5, 3])

with c30:

    # st.caption("")
    st.image("assets/test.png", width=90)

with c32:

    st.title("중대재해처벌법 Quiz")
    st.caption("중대재해처벌법에 대한 이해를 돕는 퀴즈풀이")


tabQuiz, tabAnswer = st.tabs(["문제", "답"])

with tabQuiz:
    st.title("퀴즈")
    with open("assets/중대재해퀴즈.md", "r") as file:
        file_content = file.read()
        st.markdown(file_content, unsafe_allow_html=False, help=None)

with tabAnswer:
    st.title("정답확인")
    with open("assets/중대재해퀴즈_답.md", "r") as file:
            file_content = file.read()
            st.markdown(file_content, unsafe_allow_html=False, help=None)