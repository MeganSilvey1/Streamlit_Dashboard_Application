chart = alt.Chart(df).mark_area().encode(
    x=alt.X('Year:O', axis=alt.Axis(title='Year')),
    y=alt.Y('sum(Total):Q', stack='zero', axis=alt.Axis(title='Total')),
    color='Category:N'
).transform_calculate(
    Total='datum["Expensed Equipment"] + datum["Supplies"] + datum["Computer Services"] + datum["Equipment Maintenance"] + datum["Building Maintenance"] + datum["Utilities"]'
).transform_fold(
    ["Expensed Equipment", "Supplies", "Computer Services", "Equipment Maintenance", "Building Maintenance", "Utilities"],
    as_=['Category', 'Total']
).properties(
    width=600,
    height=400
)
chart = chart.properties(title='Build and Supply Expenses by Year')
chart = chart.properties(title='Building and Supply Expenses by Year')