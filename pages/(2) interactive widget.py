import streamlit as st
from datetime import datetime
import pandas as pd

# 제목 설정
st.title("Interactive widget")
st.divider()

# 텍스트 입력 위젯
name = st.text_input(label="이름을 적어주세요!:D")
if name != "":
    st.write(f"{name}님 안녕하세요!")

# 로그인 위젯
my_id = 'python21'
my_passwd = '123456'
input_id = st.text_input("ID:")
input_passwd = st.text_input("PW:", type="password")
if my_id == input_id and my_passwd == input_passwd:
    st.success("로그인에 성공했습니다.")
else:
    st.warning('아이디 또는 비밀번호가 일치하지 않아요.')

# 숫자 입력 위젯
import random

# 학생 수 입력
num_students = st.number_input("학생 수를 입력해주세요.", min_value=0, max_value=100, step=1, format='%d')
st.write(f"학생 수는 {num_students}입니다. ")

st.divider()
# 날짜 입력 위젯
# input_date = st.date_input("오늘 날짜를 입력해주세요.")

# 요일 확인 미니 프로젝트
input_date = st.date_input("요일을 찾고 싶은 날짜를 입력해주세요.")
if input_date:
    try:
        day_of_week = input_date.strftime("%A")  # %A는 요일을 풀네임으로 표시합니다.
        st.write(f"{input_date.strftime('%Y%m%d')}의 요일은 {day_of_week} 입니다.")
    except ValueError:
        st.error("올바른 날짜 형식을 입력해주세요. (예: 2023-12-12)")

# 버튼 위젯
if st.button("버튼을 누르면 뭐가 나올까요??", type='primary'):
    st.write("# 😍")
    st.balloons()
else:
    st.write("# 🙄")

if st.button("버튼을 누르면 뭐가 나올까요?", type='primary'):
    st.write("# 😍")
    st.snow()
else:
    st.write("# 🙄")

# # 파일 업로더 위젯
# data = st.file_uploader("csv 파일을 올려주세요.")
# if data is not None:
#     st.write(pd.read_csv(data))
# st.divider()

import time

# 체크박스
if st.checkbox("텍스트를 보여줄까요?"):
    st.write("체크박스가 선택되었습니다!")

# 라디오 버튼
radio_option = st.radio("당신의 선택은?", ["A", "B", "C"])
st.write(f"당신은 {radio_option}을(를) 선택하셨습니다.")

# 멀티선택
options = st.multiselect("어떤 색상을 좋아하나요?", ["Red", "Green", "Blue"])
st.write(f"당신이 선택한 색상: {', '.join(options)}")

# 프로그레스 바
'start your progress'
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)  # 0.01초마다 프로그레스 바가 업데이트됩니다.
    my_bar.progress(percent_complete + 1)
