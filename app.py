import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pycountry

st.title('How rich are you really?')

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [100000, 20, 30, 40]
})
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

option = st.sidebar.selectbox(
    'Which country do you live in?',
     [x.name for x in list(pycountry.countries)])

income = st.sidebar.number_input(label='Your monthly income in $USD:', help="IN USD", step=100, min_value=0)

wealth = st.sidebar.number_input(label='Your net worth is $USD:', step=200, min_value=0)

"Your inncome is ", income 

'You selected:', option