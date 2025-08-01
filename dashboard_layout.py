# Place Profit_by_Year at the top of the dashboard
st.altair_chart(Profit_by_Year)

# Create a container to hold Revenue_and_Payroll and Taxes_by_Country next to each other
col1, col2 = st.columns(2)
with col1:
    st.altair_chart(Revenue_and_Payroll)
with col2:
    st.altair_chart(Taxes_by_Country)

# Put Expenses_by_Year below the charts
st.altair_chart(Expenses_by_Year)