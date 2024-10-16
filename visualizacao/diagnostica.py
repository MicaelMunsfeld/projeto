import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Carregar a base de dados
df = pd.read_csv('data/BaseCorrigida.csv')

# Tratar valores nulos
df.fillna({'arbitro': 'Desconhecido', 'time_mandante': 'Desconhecido', 'estadio': 'Desconhecido'}, inplace=True)
df.fillna(0, inplace=True)  # Preencher NaN em colunas numéricas com 0

# Converter a coluna 'data' para datetime e extrair mês e ano
df['data'] = pd.to_datetime(df['data'], errors='coerce')  # Converte a coluna 'data' para datetime
df['mes'] = df['data'].dt.month  # Extrai o mês da data
df['ano'] = df['data'].dt.year  # Extrai o ano da data

# Configuração das colunas de seleção
cols = st.columns(4)
coluna = cols[0].selectbox(
    'Dimensões Coluna',
    df.columns.tolist()
)
conteudo = cols[1].selectbox(
    'Classe:',
    df[coluna].unique()
)
medida = cols[2].selectbox(
    'Medida',
    df.select_dtypes(include=['int', 'float']).columns.tolist()
)
mes = cols[3].selectbox(
    'Mês',
    df['mes'].sort_values().unique()
)

# Filtrar dados do mês selecionado
mes_atual = df[
    (df['ano'] == df['ano'].max()) & (df['mes'] == mes)
]

cols = st.columns([1, 3])
cols[0].subheader(f'Métrica de {medida} no mês {mes}')

# Comparação com o mês anterior
if mes == 1:
    cols[0].metric(
        label=f'{medida} em relação ao mês anterior',
        value=round(mes_atual[medida].sum(), 2)
    )
else:
    mes_anterior = df[
        (df['ano'] == df['ano'].max()) & (df['mes'] == mes - 1)
    ]
    cols[0].metric(
        label=f'{medida} em relação ao mês anterior',
        value=round(mes_atual[medida].sum(), 2),
        delta=str(round(mes_atual[medida].sum() - mes_anterior[medida].sum(), 2)),
    )

# Comparação com o ano anterior
mes_ano_anterior = df[
    (df['ano'] == df['ano'] - 1) & (df['mes'] == mes)
]
cols[0].metric(
    label=f'{medida} em relação ao mês no ano anterior',
    value=round(mes_atual[medida].sum(), 2),
    delta=str(round(mes_atual[medida].sum() - mes_ano_anterior[medida].sum(), 2)),
)

# Boxplot
cols[0].subheader(f'Comparativo em {coluna}')
cols[0].plotly_chart(
    px.box(
        mes_atual,
        x=coluna,
        y=medida
    )
)

# Teste Tukey HSD
if mes_atual[coluna].nunique() >= 2:
    tukeyhsd = pairwise_tukeyhsd(endog=mes_atual[medida], groups=mes_atual[coluna], alpha=0.05)
    tukey = pd.DataFrame({
        'grupo1': tukeyhsd.groupsunique[:-1],
        'grupo2': tukeyhsd.groupsunique[1:],
        'reject': tukeyhsd.reject[:len(tukeyhsd.groupsunique) - 1],
        'meandiffs': tukeyhsd.meandiffs[:len(tukeyhsd.groupsunique) - 1]
    })
    cols[0].dataframe(tukey, use_container_width=True, hide_index=True)
else:
    st.warning("Tukey HSD requer pelo menos dois grupos distintos para comparação.")
