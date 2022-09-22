import streamlit as st
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r'C:\Users\gaith\Documents\data-spec\data-proj-5\starter\supermarket.csv')
top_data=df.sort_values('store_sales', ascending=False).head(10)

st.title("Howdy's Market Sales Data")

st.header("Top Performers")
st.subheader("Top 10 Stores") #bar
st.bar_chart(data=top_data, x='store_id', y='store_sales')
st.subheader("Average Sale Per Customer") #gauge
st.metric(label="USD", value="121.00")
st.header("Bottom Performers") 
bottom_data=df.sort_values('store_sales', ascending=True).head(10)
st.subheader("Bottom 10 Stores") #bar
st.bar_chart(data=bottom_data, x='store_id', y='store_sales')
st.subheader("Average Sale Per Customer") #gauge
st.metric(label="USD", value="21.00")
st.header("Average Sale Per Customer Overall") #gauge
st.metric(label="USD", value="75.00")