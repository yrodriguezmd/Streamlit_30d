import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Again, the header')
st.subheader('This is the subheader')
st.caption('And this is a caption')
st.markdown('While this is a markdown')
st.text('This is a text')
st.latex('Go figure, this is a latex')
st.code('And this one is a code')
st.write('Which are just variations of write.')

st.write('Hello Neo! :sunglasses:')

st.write(123456)

df = pd.DataFrame({
    'A': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'B': ['cat','dog','mouse','bird','giraffe', 'monkey', 'dragon'],
    'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6 , 0.7]
})
st.write(df)

st.write('The following is a dataframe', df, 'that is multivariate.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', color = 'c', tooltip= ['a','b','c']
)
st.write('Here is an illustration of plotting for df2:', df2)
st.write(c)

#pip install matplotlib
#import matplotlib.pyplot as plt
#df2.plot(kind = 'scatter', x = 'a',y = 'b');
#df2[['a','b']].plot(kind='bar');
#plt.bar(df2['b'], height = 'a');