import streamlit as st
import matplotlib.pyplot as plt

def show_visuals(df):
    """Displays key visual insights from the cleaned dataset."""
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
    st.write("**Column Data Types:**")
    st.write(df.dtypes)

    selected_col = st.selectbox("📈 Select a column to visualize:", df.columns)

    if df[selected_col].dtype in ['int64', 'float64']:
        st.markdown(f"#### Histogram for `{selected_col}`")
        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=10, color='#00b4d8', edgecolor='black')
        st.pyplot(fig)
    else:
        st.markdown(f"#### Category Count for `{selected_col}`")
        value_counts = df[selected_col].value_counts()
        st.bar_chart(value_counts)

    st.write("### 🔍 Summary Statistics")
    st.write(df.describe())
