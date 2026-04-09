import streamlit as st

st.title("Phishing Detection App")

url = st.text_input("Enter URL")

if st.button("Check"):
    st.write("Checking URL...")
