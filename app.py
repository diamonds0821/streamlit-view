import streamlit as st

st.write('# 미다스하우징 데이터')
st.write('#### 기간: 2023.01.01 - 2023.01.09 ')

import pandas as pd
df = pd.read_csv('c:/data/230110.csv',thousands = ',')
df1 = df.replace(['현매', 'DC'],['매출','반품'])
df2 = df1.drop(615)
df3 = df2.astype({'수량':int})
df4 = pd.pivot_table(df3, index='전표일자', columns='담당자', values=['총금액'], aggfunc='sum')
df4