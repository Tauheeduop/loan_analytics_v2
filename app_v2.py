import streamlit as st
import pandas as pd
from modules.data_cleaner import clean_data
from modules.data_visualizer import show_visuals



# ------------------ Page Setup ------------------ #
st.set_page_config(page_title="Loan Analytics v2", layout="wide")

st.title("🏦 Loan Approval Insight Dashboard (v2.0)")
st.markdown("This dashboard explores and cleans loan approval data interactively.")

# ------------------ Load Dataset ------------------ #
uploaded_file = st.file_uploader("📂 Upload your loan dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")

    # ------------------ Data Cleaning ------------------ #
    st.markdown("### 🧹 Data Cleaning")
    df_clean = clean_data(df)
    st.write(df_clean.head())

    # ------------------ Visual Insights ------------------ #
    st.markdown("### 📊 Data Visualization & Insights")
    show_visuals(df_clean)

else:
    st.info("👆 Please upload a dataset to begin.")
