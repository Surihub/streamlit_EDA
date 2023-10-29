import streamlit as st

st.title("Exploratory Data Analysis")
st.write("Hello, statistics!")

name = st.text_input("이름을 입력해주세요.")
if name != "":
    st.write(f"반가워요, {name}님!")
    st.write("# 😃")