import streamlit as st
import pandas as pd

def main():
   df = pd.read_csv('c:/data/230110.csv')
   st.dataframe(df)
   st.dataframe(df.style.highlight_max(axis=0))
   st.table(df)

   st.table(df.head())
   st.write(df.head())
   st.text(df.head())


if __name__ == '__main__':
   main()
