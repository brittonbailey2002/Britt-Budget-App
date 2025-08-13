
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget Calculator", layout="centered")

st.title("💰 Budget Calculator")
st.write("Track your income, expenses, and savings with ease.")

# User inputs
income = st.number_input("Monthly Income ($)", min_value=0, value=3600, step=100)
groceries_eating_out = st.number_input("Groceries & Eating Out ($)", min_value=0, value=600, step=50)
gas = st.number_input("Gas ($)", min_value=0, value=200, step=20)
utilities = st.number_input("Utilities ($)", min_value=0, value=150, step=10)
rent = st.number_input("Rent/Mortgage ($)", min_value=0, value=900, step=50)
ring_payment = st.number_input("Ring Payment ($)", min_value=0, value=433, step=10)
misc = st.number_input("Miscellaneous ($)", min_value=0, value=200, step=20)

# Calculations
total_expenses = groceries_eating_out + gas + utilities + rent + ring_payment + misc
savings = income - total_expenses

# Display results
st.subheader("Summary")
data = {
    "Category": ["Income", "Total Expenses", "Savings"],
    "Amount ($)": [income, total_expenses, savings]
}
df = pd.DataFrame(data)
st.table(df)

# Monthly savings projection
if savings > 0:
    st.success(f"You are saving ${savings} per month! At this rate, you'll save ${savings * 12} in a year.")
else:
    st.error("You are spending more than you earn. Consider adjusting your expenses.")
