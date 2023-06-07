import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest

st.title('ZTEST')

with st.expander('view data'):
    df = pd.read_csv('https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv')
    st.dataframe(df.transpose())

with st.expander('view statistic'):
    st.dataframe(df.describe().transpose())

st.write('## Constructing Hypothesis')
st.latex('H_{0} : \mu = \mu_{0}')
st.latex('H_{1} : \mu \neg \mu_{0}') #\neg stands 

alpha = st.number_input('masukkan nilai alpha', step=0.0001, min_value=0., max_value=1.)
null_mean = st.number_input('masukkan nilai mu', step=0.0001)

clicked = st.button('do the Z test!!')

if clicked:
    alpha_z = NormalDist().inv_cdf(p=1-alpha/2)
    z_score, p_value = ztest(df['grades'], value=null_mean, alternative='two-sided')
    if abs(z_score) > alpha_z:
        st.latex('REJECT H_{0}')
    else:
        st.latex('CAN NOT REJECT H_{0}')
    st.write(f'titik kritis = {alpha_z}, hitung z = {z_score}, p_value = {p_value}')


st.write()