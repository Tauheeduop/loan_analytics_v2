import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# ------------------ Page Setup ------------------ #
st.set_page_config(page_title="Loan Analytics Dashboard Version 2.0", layout="wide")
# ------------------ Load CSS ------------------ #
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# ------------------ Title ------------------ #
st.title(" Loan Analytics Dashboard — Version 2.0 (AI Insights)")
st.markdown("<hr>", unsafe_allow_html=True)
# ------------------ Data ------------------ #
data = [
    {"Name": "Naveed", "Loan Amount": 40000, "Interest Rate": 10},
    {"Name": "Ahmad", "Loan Amount": 55000, "Interest Rate": 12},
    {"Name": "Sara", "Loan Amount": 30000, "Interest Rate": 8},
    {"Name": "Hina", "Loan Amount": 70000, "Interest Rate": 15},
    {"Name": "Usman", "Loan Amount": 25000, "Interest Rate": 7},
    {"Name": "Tauheed", "Loan Amount": 55000, "Interest Rate": 17}
]
df = pd.DataFrame(data)

# ------------------ KPI Calculations ------------------ #
total_loan = df["Loan Amount"].sum()
avg_loan = df["Loan Amount"].mean()
highest_loan = df["Loan Amount"].max()
num_borrowers = len(df)
high_value_borrowers = len(df[df["Loan Amount"] > 50000])

# ------------------ KPI Cards ------------------ #
st.markdown("<div class='section-title'>📊 Key Performance Indicators</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

col1.markdown(f"<div class='kpi-card kpi-total'>💵 Total Loan<div class='kpi-value'>{total_loan:,}</div></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='kpi-card kpi-avg'>📈 Avg Loan<div class='kpi-value'>{avg_loan:,.0f}</div></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='kpi-card kpi-highest'>💰 Highest Loan<div class='kpi-value'>{highest_loan:,}</div></div>", unsafe_allow_html=True)
col4.markdown(f"<div class='kpi-card kpi-borrowers'>👥 Borrowers<div class='kpi-value'>{num_borrowers}</div></div>", unsafe_allow_html=True)
col5.markdown(f"<div class='kpi-card kpi-highvalue'>⭐ High Value<div class='kpi-value'>{high_value_borrowers}</div></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ------------------ Data Overview ------------------ #
st.markdown("<div class='section-title'>📋 Loan Data Overview</div>", unsafe_allow_html=True)
#st.dataframe(df, use_container_width=True)
st.dataframe(df, width='stretch')


# ------------------ Chart ------------------ #
fig, ax = plt.subplots(figsize=(7,4))
ax.bar(df["Name"], df["Loan Amount"], color="#4B9CD3", edgecolor="black")
ax.set_title("Loan Amount by Person", fontsize=14, fontweight='bold', color='#003366')
ax.set_xlabel("Name")
ax.set_ylabel("Loan Amount")
st.pyplot(fig)

# ------------------ Insights ------------------ #
highest_interest = df.loc[df["Interest Rate"].idxmax()]
high_value_names = df[df["Loan Amount"] > 50000]["Name"].tolist()

st.markdown("<div class='section-title'> Insights Summary</div>", unsafe_allow_html=True)
st.write(f"- **Highest Interest Loan:** {highest_interest['Name']} ({highest_interest['Interest Rate']}%)")
st.write(f"- **High Value Borrowers (>50K):** {', '.join(high_value_names) if high_value_names else 'None'}")

st.success(" Dashboard Ready — Styled with external CSS!")

st.markdown("<footer>Designed with using Streamlit | Tauheed's Loan Analytics Project</footer>", unsafe_allow_html=True)
