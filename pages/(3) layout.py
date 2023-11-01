# Streamlit 라이브러리를 임포트합니다.
import streamlit as st

# 웹 페이지의 제목을 설정합니다.
st.title("Layout")
# 웹 페이지의 제목 아래에 구분선을 추가합니다.
st.divider()

# 사이드바의 상단에 헤더를 추가합니다.
st.sidebar.header('사이드바 헤더')
# 사이드바에 0부터 100까지의 값을 선택할 수 있는 슬라이더를 생성하고, 선택된 값을 number 변수에 할당합니다.
number = st.sidebar.slider("사이드바 슬라이더", 0, 100)

# 웹 페이지에 4개의 동등한 너비의 컬럼을 생성합니다.
wid = 150
col1, col2, col3, col4 = st.columns(4)
# 각 컬럼에 다른 이모티콘을 표시합니다.
with col1:
    st.write("# 😀")
with col2:
    st.write("# 😂")
with col3:
    st.write("# 🤩")
with col4:
    st.write("# 😶")

# 웹 페이지에 '봄', '여름', '가을', '겨울' 네 개의 탭을 생성합니다.
wid = 500
tab1, tab2, tab3, tab4 = st.tabs(['봄', '여름', '가을', '겨울'])
# 각 탭에 해당하는 내용을 추가합니다.
with tab1:
    st.write("# 내용을 입력하세요.💐")
with tab2:
    st.write("# 내용을 입력하세요.🌊")
with tab3:
    st.write("# 내용을 입력하세요.🍁")
with tab4:
    st.write("# 내용을 입력하세요.⛄")

st.divider()
# 클릭하면 내용이 펼쳐지는 확장 패널을 생성합니다.
with st.expander("여기를 클릭하면 내용이 펼쳐집니다"):
    st.write("확장된 내용이 여기에 표시됩니다.")
