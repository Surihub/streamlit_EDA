# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import pandas as pd
import numpy as np

# 웹 페이지의 제목 및 헤더를 설정합니다.
st.title(":blue[Beautiful] Data display")

# 텍스트 및 코드 블록 섹션
st.title("텍스트 & 코드 블록")
st.header("st.title 보다 작은 제목 형식")
st.subheader("st.header 보다 작은 제목 형식")
st.caption("캡션을 입력해주세요.")
st.code("print('hello')# 코드 입력하듯이 입력해주세요")
code = '''print("hello")# 코드 입력
print("World")# 여러 줄인 경우'''
st.code(code, language='python')  # Python 코드로 표시
st.text("hello again_text")
st.write("hello again_write")
st.latex("2+1=3")
st.latex(r'''ax^2+bx+c=0''', help='이차방정식')  # 이차방정식 수식
st.divider()

# 이미지 및 비디오 섹션
st.title("미디어")
st.image("https://upload.wikimedia.org/wikipedia/ko/4/4a/%EC%8B%A0%EC%A7%B1%EA%B5%AC.png")
st.image("https://upload.wikimedia.org/wikipedia/ko/4/4a/%EC%8B%A0%EC%A7%B1%EA%B5%AC.png",
         width=200, caption='짱구')  # 이미지 크기와 캡션 설정
st.video("https://www.youtube.com/watch?v=Inkr9_3arto&pp=ygUQ7ZmU7KKAIO2SgOyWtOu0kA%3D%3D",
         start_time=10)  # 10초부터 비디오 재생
st.divider()

# 데이터 표시 섹션
st.title("데이터 표시")
df = pd.DataFrame(np.random.rand(4, 5), columns=['a', 'b', 'c', 'd', 'e'])
st.dataframe(df)
st.table(df)  # 상호작용이 없는 테이블로 표시
st.write(df.style.highlight_max())
col1, col2 = st.columns(2)
col1.metric("온도", "12.4℃", "1.2℃")
col2.metric("온도", "12.4℃", "1.2℃")
st.divider()

# 소수 판별기 섹션
st.title("소수 판별기")
def is_prime(num):
    """주어진 수가 소수인지 판별하는 함수"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            st.write(f"적어도 약수로 {i}를 갖고있네요!")
            return False
    return True

num = st.number_input("자연수를 입력하세요", min_value=1, value=1, step=1)
if st.button("소수 판별"):
    if is_prime(num):
        st.success(f"{num}은(는) 소수입니다!")  # 성공 메시지 표시
    else:
        st.warning(f"{num}은(는) 소수가 아닙니다.")  # 경고 메시지 표시
