import altair as alt

chart1 = alt.Chart(df).mark_bar(color='blue').encode(
    x=alt.X('Hotel ID:N', title='Hotel ID'),
    y=alt.Y('sum(Revenue):Q', title='Revenue and Annual Payroll')
).properties(
    title='Total Revenue by Hotel ID'
)

chart2 = alt.Chart(df).mark_bar(color='red').encode(
    x=alt.X('Hotel ID:N', title='Hotel ID'),
    y=alt.Y('sum(Annual payroll):Q')
).properties(
    title='Total Annual Payroll by Hotel ID'
)

chart = chart1 + chart2
