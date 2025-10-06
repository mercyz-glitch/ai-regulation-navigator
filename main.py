import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="AI Regulation Navigator", layout="wide")

st.title("🧭 AI Regulation Navigator – MVP by Mercy")

st.markdown("""
Welcome to the AI Regulation Navigator MVP.  
This tool is designed to quickly assess AI compliance maturity across key categories and visualize it via a radar chart.
""")

# --- Sidebar Input ---
st.sidebar.header("Company Profile")
industry = st.sidebar.selectbox("Select Industry", ["Healthcare", "Automotive", "Finance", "Software", "Other"])
company_size = st.sidebar.selectbox("Company Size", ["1-10", "11-50", "51-200", "201-500", "500+"])
location = st.sidebar.text_input("Location", "Germany")

st.sidebar.markdown("---")
st.sidebar.subheader("Maturity Assessment")
governance = st.sidebar.slider("Governance", 0, 5, 2)
risk = st.sidebar.slider("Risk Management", 0, 5, 2)
transparency = st.sidebar.slider("Transparency", 0, 5, 2)
data_quality = st.sidebar.slider("Data Quality", 0, 5, 2)
bias = st.sidebar.slider("Bias & Fairness", 0, 5, 2)

# --- Data and Radar Chart ---
criteria = ['Governance', 'Risk', 'Transparency', 'Data Quality', 'Bias']
scores = [governance, risk, transparency, data_quality, bias]

df = pd.DataFrame(dict(
    r=scores + [scores[0]],
    theta=criteria + [criteria[0]]
))

st.subheader("🔍 Compliance Radar Chart")
fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(df['theta'], df['r'], marker='o')
ax.fill(df['theta'], df['r'], alpha=0.25)
ax.set_ylim(0, 5)
st.pyplot(fig)

# --- Interpretation ---
st.subheader("📝 AI Compliance Summary")

def interpret(score):
    if score >= 4:
        return "✔️ Compliant"
    elif score >= 2:
        return "⚠️ Partial Compliance"
    else:
        return "❌ Non-Compliant"

interpretations = [interpret(s) for s in scores]

summary_df = pd.DataFrame({
    "Category": criteria,
    "Score (0–5)": scores,
    "Status": interpretations
})

st.table(summary_df)

st.markdown("✅ **This tool is for demo purposes only. Not legal advice.**")
