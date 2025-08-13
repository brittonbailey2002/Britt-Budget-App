# Britt-Budget-App
Monthly budget app to help keep track of your income, expenses, and savings each month.

import streamlit as st
import pandas as pd

st.title("Britton's Monthly Budget Calculator")

# Budget data
budget_data = {
    "Category": [
        "Rent + Utilities",
        "Ring Payment",
        "Food (Groceries + Eating Out)",
        "Savings (House + Emergency)",
        "Miscellaneous",
        "Transportation / Gas",
    ],
    "Budgeted ($)": [755, 130, 800, 1785, 200, 350],
}

df = pd.DataFrame(budget_data)
df["Actual ($)"] = 0
df["Difference ($)"] = 0

st.write("Enter your actual expenses:")

actuals = []
for idx, row in df.iterrows():
    actual = st.number_input(f"{row['Category']}", min_value=0.0, step=10.0)
    actuals.append(actual)

df["Actual ($)"] = actuals
df["Difference ($)"] = df["Budgeted ($)"] - df["Actual ($)"]

st.write("### Budget Summary")
st.dataframe(df.style.format({"Budgeted ($)": "${:,.2f}", "Actual ($)": "${:,.2f}", "Difference ($)": "${:,.2f}"}))

total_budgeted = df["Budgeted ($)"].sum()
total_actual = df["Actual ($)"].sum()
total_diff = total_budgeted - total_actual

st.write(f"**Total Budgeted:** ${total_budgeted:,.2f}")
st.write(f"**Total Actual:** ${total_actual:,.2f}")
st.write(f"**Total Difference:** ${total_diff:,.2f} (Positive means under budget)")

st.write("---")
st.write("Keep track monthly and adjust your spending to meet your goals!")

