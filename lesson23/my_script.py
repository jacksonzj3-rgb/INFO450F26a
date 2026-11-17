
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('lesson23/Advertising_F.csv')

st.title("Advertising Effectiveness Zion")

st.sidebar.header("Filters")
x_var = st.sidebar.selectbox("X axis", ["TV", "newspaper"])

#show scatterplot
fig = px.scatter(df, x=x_var, y="sales",
                 labels={'TV':'Tv ad spend','radio':'Radio ad spend'})

st.plotly_chart(fig)

#show the barplot
sales_per_city = df.groupby('City')['sales'].sum().reset_index()

fig = px.bar(sales_per_city, x='City', y="sales", title="data is fun")

st.plotly_chart(fig)

#show the dataframe
st.dataframe(df)

