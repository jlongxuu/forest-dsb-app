# app.py
import streamlit as st
import pandas as pd
from src.dataset import load_train_all, load_test

st.set_page_config(page_title="Forest DSB - Demo", layout="wide")
st.title("Forest DSB - Streamlit App")

@st.cache_data(show_spinner=False)
def get_data():
    train = load_train_all()
    test = load_test()
    return train, test

try:
    train, test = get_data()
    st.subheader("Train summary")
    st.write(train.shape)
    st.dataframe(train.head())

    st.subheader("Test summary")
    st.write(test.shape)
    st.dataframe(test.head())

    # simple screening
    with st.expander("Describe train"):
        st.write(train.describe(include="all"))
except FileNotFoundError as e:
    st.error(f"Data file not found: {e}")
    st.info("make sure data is in data/forest-dsb-*/ ")

