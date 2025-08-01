import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x='Country',
    y='sum(Taxes and license fees)'
).properties(
    title='Total Taxes and License Fees by Country',
    width=600,
    height=400
)
chart = chart.configure_mark(color='purple')