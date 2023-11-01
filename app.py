import streamlit as st

st.title("숩숩의 페이지")
st.header("Hello, statistics!")

name = st.text_input("이름이 무엇인가요?")
if name != "":
    st.write(f"# 😃 반가워요, {name}님!")
    st.balloons()
    