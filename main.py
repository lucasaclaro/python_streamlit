import streamlit as st
import pandas as pd

st.set_page_config(page_title='PIB Araraquara')

with st.container():
    st.subheader('Estudos econômicos')
    st.title('Araraquara/SP - Produto Interno Bruto ')
    st.write('Informações sobre o PIB no município de Araraquara/SP (ano 2002  - 2018)')

@st.cache_data
def load_data():
    data = pd.read_csv('data/municipio.csv')
    data_base = data.query('id_municipio == 3503208')
    return data_base

with st.container():
    st.write('---')


    city = load_data()
    st.area_chart(data=city, x='ano', y='pib')





#streamlit run main.py - rodar o site