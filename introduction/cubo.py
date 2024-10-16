import pandas as pd
import streamlit as st

cols = st.columns(4)
linha = cols[0].multiselect(
    'Dimensões Linhas',
    st.session_state['dimensao']
)
colunas = cols[1].multiselect(
    'Dimensões Colunas',
    st.session_state['dimensao']
)
valor = cols[2].selectbox(
    'Medidas',
    st.session_state['medida']
)
agg = cols[3].selectbox(
    'Agregador',
    st.session_state['agregador']
)

if(len(linha) > 0) & (len(colunas) > 0) & (linha != colunas):
    st.dataframe(
        st.session_state['dif'].pivot_table(
            index=linha,
            columns=colunas,
            values=valor,
            aggfunc=agg,
            fill_value=0
        )
    )
    st.dataframe(
        st.session_state['dif'].groupby(linha)[valor].sum().reset_index()
    )
