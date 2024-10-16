import pandas as pd
import streamlit as st

@st.cache_data
def load_database():
    df = pd.read_csv('data/BaseCorrigida.csv', encoding='utf-8', delimiter=',')
    return df

st.set_page_config(page_title="Brasileirão Pontos corridos", layout="wide")
st.session_state['df'] = load_database()
st.session_state['dimensao'] = ['ano_campeonato', 'estadio', 'time_mandante', 'time_visitante']
st.session_state['dimensao_tempo'] = ['data', 'rodada']
st.session_state['medida'] = ['publico', 'chutes_mandante', 'chutes_visitante']
st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']
st.title('Brasileirão Pontos corridos (2003 - 2023)')

pg = st.navigation(
    {
        "Introdução": [
            st.Page(page='introducao/tabela.py', title='Tabela', icon=':material/house:'),
            st.Page(page='introducao/cubo.py', title='Cubo', icon=':material/help:'),
            # st.Page(page='introducao/dashboard.py', title='Dashboard', icon=':material/help:'),
            st.Page(page='introducao/visualizacao.py', title='Visualização', icon=':material/help:')
        ],
        "Visualização": [
            st.Page(page='visualizacao/descritiva.py', title='Análise Descritiva', icon=':material/house:'),
            st.Page(page='visualizacao/diagnostica.py', title='Análise Diagnóstica', icon=':material/help:'),
            ##st.Page(page='visualizacao/preditiva.py', title='Análise Preditiva', icon=':material/help:'),  
            ##st.Page(page='visualizacao/prescritiva.py', title='Análise Prescritiva', icon=':material/help:')  
        ]
    }
)
pg.run()