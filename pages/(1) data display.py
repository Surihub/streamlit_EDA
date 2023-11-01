import streamlit as st
import pandas as pd
import numpy as np

# 제목 및 헤더 설정
st.title(":blue[Beautiful] Data display")
st.header("st.title 보다 작은 제목 형식")
st.subheader("st.header 보다 작은 제목 형식")
st.caption("캡션을 입력해주세요.")

# 코드 블록 표시
st.code("print('hello')# 코드 입력하듯이 입력해주세요")
code = '''print("hello")# 코드 입력
print("World")# 여러 줄인 경우'''
st.code(code, language='python')

# 텍스트 표시
st.text("hello again_text")
st.write("hello again_write")

# 수식 표시
st.latex("2+1=3")
st.latex(r'''ax^2+bx+c=0''', help='이차방정식')

# 구분선 표시
st.divider()
st.write("----")

# 이미지 및 비디오 표시
st.image("https://upload.wikimedia.org/wikipedia/ko/4/4a/%EC%8B%A0%EC%A7%B1%EA%B5%AC.png")
st.image("https://upload.wikimedia.org/wikipedia/ko/4/4a/%EC%8B%A0%EC%A7%B1%EA%B5%AC.png",
         width=200, caption='짱구')
st.video("https://www.youtube.com/watch?v=Inkr9_3arto&pp=ygUQ7ZmU7KKAIO2SgOyWtOu0kA%3D%3D",
         start_time=10)

# 데이터 프레임 표시
df = pd.DataFrame(np.random.rand(4, 5), columns=['a', 'b', 'c', 'd', 'e'])
st.dataframe(df)
st.write(df)
st.table(df)  # not interactive

# 최대값 하이라이트
st.write(df.style.highlight_max())

# 메트릭 표시
col1, col2 = st.columns(2)
col1.metric("온도", "12.4℃", "1.2℃")
col2.metric("온도", "12.4℃", "1.2℃")
st.divider()
