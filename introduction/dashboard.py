import streamlit as st
import pygwalker as pyg

st.title('Dashboard Interativo com Pygwalker')

df = st.session_state['dif']

# Renderizando o dataframe com Pygwalker
pyg.walk(df)
