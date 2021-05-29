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

'You selected:', option