import streamlit as st
import pandas as pd

st.title("Upload Dataset Kaggle - Analisis Sederhana")

file = st.file_uploader("Upload file CSV", type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("Dataset")
    st.dataframe(df)

    st.subheader("Statistik")
    st.write(df.describe())

    st.subheader("Kolom")
    st.write(df.columns.tolist())

    col = st.selectbox("Pilih kolom untuk analisis nilai unik", df.columns)
    st.write(df[col].value_counts())
