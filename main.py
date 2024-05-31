import pandas
import streamlit as st

st.title("Personalized Greeting App")

name = st.text_input("Enter your name:")

color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])

if st.button("Show Greeting"):
    st.markdown(f"<h2 style='color: {color};'>Hello, {name}!😃</h2>", unsafe_allow_html=True)
