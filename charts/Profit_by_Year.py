chart = alt.Chart(df).mark_line().encode(
    x='Year:O',
    y='sum(Profit):Q'
).properties(
    title='Profit by Year',
    width=600,
    height=400
)


chart = chart.encode(
    alt.Y('sum(Profit):Q', scale=alt.Scale(domain=[18000000, 22000000]))
)
chart = chart.encode(
    alt.Y("sum(Profit)", scale=alt.Scale(domain=[19000000, 21000000]))
)