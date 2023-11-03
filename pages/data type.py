import streamlit as st
import pandas as pd

# 데이터를 불러오는 함수 (여기서는 예제 데이터를 사용합니다)
@st.cache_data  # 데이터 캐싱
def load_data():
    data = {
        'Age': [25, 32, 47, 51],
        'Gender': ['Male', 'Female', 'Female', 'Male'],
        'Income': [50000, 54000, 70000, 68000]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# 각 열의 데이터 유형을 추론하는 함수
def infer_column_types(df):
    column_types = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_types[column] = 'Numeric'
        else:
            column_types[column] = 'Categorical'
    return column_types

column_types = infer_column_types(df)

# 사용자가 각 열의 데이터 유형을 설정할 수 있도록 입력 받기
user_column_types = {}
for column, col_type in column_types.items():
    user_col_type = st.selectbox(
        f"Select the column type for '{column}' (Current: {col_type})",
        ['Numeric', 'Categorical'],
        key=column
    )
    user_column_types[column] = user_col_type

# 사용자의 입력에 따라 DataFrame의 열 유형을 변환
def convert_column_types(df, user_column_types):
    for column, col_type in user_column_types.items():
        if col_type == 'Numeric':
            df[column] = pd.to_numeric(df[column], errors='coerce')  # 범주형을 수치형으로 변환
        elif col_type == 'Categorical':
            df[column] = df[column].astype('category')  # 수치형을 범주형으로 변환
    return df

# 열 유형 변환 실행
df = convert_column_types(df, user_column_types)

st.write('Data with updated column types:')
st.dataframe(df)

# 나머지 스트림릿 앱 코드...
