import pandas as pd
import streamlit as st
import sqlite3
st.set_page_config(page_title='RecallAnalysis', layout='wide')
import openai


st.title("Recall Analysis")

openai.api_key = st.secrets["openAI_SK"]


def get_data_from_DB() -> pd.DataFrame:
  con = sqlite3.connect('recall.db')
  df = pd.read_sql_query("SELECT * FROM tb_recalls", con)
  con.close()
  return df

df = get_data_from_DB()
st.dataframe(df)
