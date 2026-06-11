import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
conn = sqlite3.connect("alerts.db")

df = pd.read_sql(
    "SELECT * FROM alerts",
    conn
)

st.title("Endpoint Detection & Response")

st.dataframe(df)
st.metric(
    "Total Threats",
    len(df)
)


fig = px.bar(
    df,
    x="severity"
)

st.plotly_chart(fig)