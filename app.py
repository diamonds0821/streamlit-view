import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('c:/data/230110.csv', thousands=',')
df1 = df.iloc[:,[0,2,5,16,23]]
dataset = df1.replace({'담당자' :['반장창고','대리점']}, '강실장')
st.set_page_config(page_title='Midas Sales',layout='wide')

st.sidebar.header('Filter  by:')

category = st.sidebar.multiselect('Filter By Category:',
                                    options = dataset['담당자'].unique(),
                                    default = dataset['담당자'].unique())
selection_query = dataset.query(
   '담당자== @category'
)

st.title('미다스하우징 매출')

total_profit = (selection_query['총금액'].sum())
total_number = ((selection_query['수량'].sum()))

first_column,second_column = st.columns(2)
with first_column:
   st.markdown('# 합계:')
   st.subheader(f'{total_profit}',)

with second_column:
   st.markdown('# 수량(평)')
   st.subheader(f'{total_number}',)

st.markdown('---')

profit_by_category=(selection_query.groupby(by=["담당자"]).sum()[['총금액']])
profit_by_category_barchart = px.bar(profit_by_category,
                              x="총금액",
                              y=profit_by_category.index,
                              title='Profit By Category',
                              color_discrete_sequence =['#17f50c'],
                              )
profit_by_category_barchart.update_layout(plot_bgcolor = 'rgba(0,0,0,0)', xaxis=(dict(showgrid=False)))

profit_by_category_piechart = px.pie(profit_by_category, names = profit_by_category.index,values = '총금액', title='판매데이터', hole=.3, color_discrete_sequence=px.colors.sequential.RdPu_r)

left_column,right_column = st.columns(2)
left_column.plotly_chart(profit_by_category_barchart,use_container_width=True)
right_column.plotly_chart(profit_by_category_piechart,use_container_width=True)