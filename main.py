import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")


df = pd.read_csv("happiness_data.csv")

option1 = st.selectbox("Select the data for X-axis: ", ("Happiness", "GDP", \
"Social Support", "Life Expectancy", "Freedom to Make Life Choices", "Generosity", "Corruption"))

option2 = st.selectbox("Select the data for Y-axis: ", ("GDP", "Happiness", \
"Social Support", "Life Expectancy", "Freedom to Make Life Choices", "Generosity", "Corruption"))

match option1:
    case "Happiness":
        x_data = df["Happiness"]
    case "GDP":
        x_data = df["GDP"]
    case "Social Support":
        x_data = df["Social Support"]
    case "Life Expectancy":
        x_data = df["Life Expectancy"]
    case "Freedom to Make Life Choices":
        x_data = df["Freedom to Make Life Choices"]
    case "Generosity":
        x_data = df["Generosity"]
    case "Corruption":
        x_data = df["Corruption"]

match option2:
    case "Happiness":
        y_data = df["Happiness"]
    case "GDP":
        y_data = df["GDP"]
    case "Social Support":
        y_data = df["Social Support"]
    case "Life Expectancy":
        y_data = df["Life Expectancy"]
    case "Freedom to Make Life Choices":
        y_data = df["Freedom to Make Life Choices"]
    case "Generosity":
        y_data = df["Generosity"]
    case "Corruption":
        y_data = df["Corruption"]

st.subheader(f"The Correlation of {option1} and {option2}")
figure = px.scatter(df, x=x_data, y=y_data)
st.plotly_chart(figure)