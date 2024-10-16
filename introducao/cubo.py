import pandas as pd
import streamlit as st

# Criando as seleções para linhas, colunas, medidas e agregadores
cols = st.columns(4)
linhas = cols[0].multiselect(
    'Dimensões Linha',
    st.session_state['dimensao']
)
colunas = cols[1].multiselect(
    'Dimensões Coluna',
    st.session_state['dimensao'] + st.session_state['dimensao_tempo']
)
valor = cols[2].selectbox(
    'Medidas',
    st.session_state['medida']
)
agg = cols[3].selectbox(
    'Agregador',
    st.session_state['agregador']
)

# Função para limpar colunas de valores complexos e garantir que sejam unidimensionais
def clean_column(col):
    # Verifica se a coluna contém objetos complexos (listas, dicionários, etc.)
    if df[col].apply(lambda x: isinstance(x, (list, dict, set, pd.Series, pd.DataFrame))).any():
        st.warning(f"A coluna '{col}' contém valores complexos e será convertida para strings.")
        # Converte valores complexos para strings simples
        df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (list, dict, set, pd.Series, pd.DataFrame)) else x)
    # Remove valores nulos e espaços em branco que possam causar problemas
    df[col] = df[col].fillna('N/A').astype(str)

df = st.session_state['df'].copy()
for col in linhas + colunas:
    clean_column(col)

if (len(linhas) > 0) & (len(colunas) > 0) & (linhas != colunas):
    try:
        pivot_table = df.pivot_table(
            index=linhas,
            columns=colunas,
            values=valor,
            aggfunc=agg,
            fill_value=0
        )
        st.dataframe(pivot_table)
    except ValueError as e:
        st.error(f"Erro ao criar a tabela dinâmica: {str(e)}")
    try:
        grouped_data = df.groupby(linhas)[valor].agg(agg).reset_index()
        st.dataframe(grouped_data)
    except Exception as e:
        st.error(f"Erro ao agrupar os dados: {str(e)}")
