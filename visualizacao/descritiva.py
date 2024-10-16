import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Carregar a base de dados
df = pd.read_csv('data/BaseCorrigida.csv')

# Tratar valores nulos, preenchendo com 'Desconhecido' para colunas categóricas e 0 para numéricas
df.fillna({'arbitro': 'Desconhecido', 'time_mandante': 'Desconhecido', 'estadio': 'Desconhecido'}, inplace=True)
df.fillna(0, inplace=True)  # Preencher NaN em colunas numéricas com 0

# Converter a coluna 'data' para datetime e extrair mês e ano
df['data'] = pd.to_datetime(df['data'], errors='coerce')  # Converte a coluna 'data' para datetime
df['mes'] = df['data'].dt.month  # Extrai o mês da data
df['ano'] = df['data'].dt.year  # Extrai o ano da data

# Configuração das colunas de seleção
cols = st.columns(3)
colunas = cols[0].multiselect(
    'Dimensões Coluna',
    df.columns.tolist()
)
valor = cols[1].selectbox(
    'Medidas',
    df.select_dtypes(include=['int', 'float']).columns.tolist()
)
cor = cols[2].selectbox(
    'Cor',
    colunas
)

# Verificar se há valores válidos para a coluna de medidas
if df[valor].sum() == 0:
    st.warning(f"A coluna '{valor}' não contém valores suficientes para gerar o gráfico.")
else:
    # Tabs para diferentes tipos de gráficos
    tabs = st.tabs(['Treemap', 'Sunburst', 'Sankey', 'TimeSeries'])

    if len(colunas) > 2:
        with tabs[0]:
            # Treemap
            fig = px.treemap(
                df,
                path=colunas,
                values=valor,
                color=cor,
                height=800,
                width=1200
            )
            fig.update_traces(textinfo='label+value')
            st.plotly_chart(fig)

        with tabs[1]:
            # Sunburst
            fig = px.sunburst(
                df,
                path=colunas,
                values=valor,
                color=cor,
                height=800,
                width=1200
            )
            fig.update_traces(textinfo='label+value')
            st.plotly_chart(fig)

        with tabs[2]:
            # Sankey
            grupo = df.groupby(colunas)[valor].sum().reset_index().copy()
            rotulos, codigo = [], 0
            for coluna in colunas:
                for conteudo in grupo[coluna].unique():
                    rotulos.insert(len(rotulos), [codigo, conteudo])
                    codigo += 1
            rotulos = pd.DataFrame(rotulos, columns=['codigo', 'conteudo'])
            rotulos['codigo'] = rotulos['codigo'].astype(int)
            sankey = []
            for i in range(0, len(colunas) - 1):
                for index, row in grupo.iterrows():
                    sankey.insert(
                        len(sankey),
                        [
                            rotulos[rotulos['conteudo'] == row[colunas[i]]]['codigo'].values[0],
                            rotulos[rotulos['conteudo'] == row[colunas[i+1]]]['codigo'].values[0],
                            row[valor],
                            row[valor]
                        ]
                    )
            sankey = pd.DataFrame(sankey, columns=['source', 'target', 'value', 'label'])
            data_trace = dict(
                type='sankey', domain=dict(x=[0, 1], y=[0, 1]),
                orientation="h",
                valueformat=".2f",
                node=dict(pad=10, thickness=30, line=dict(color="black", width=0.5),
                    label=rotulos['conteudo'].to_list()
                ),
                link=dict(
                    source=sankey['source'].dropna(axis=0, how='any'),
                    target=sankey['target'].dropna(axis=0, how='any'),
                    value=sankey['value'].dropna(axis=0, how='any'),
                    label=sankey['label'].dropna(axis=0, how='any'),
                )
            )
            layout = dict(
                title="Hierarquias",
                height=800,
                width=1200,
                font=dict(
                    size=10
                ),
            )
            fig = go.Figure(dict(data=[data_trace], layout=layout))
            st.plotly_chart(fig)

        with tabs[3]:
            # TimeSeries
            for coluna in colunas:
                base = df.pivot_table(index='data', columns=coluna, values=valor, aggfunc='sum').reset_index()
                st.plotly_chart(
                    px.line(
                        base,
                        x='data',
                        y=base.columns,
                    )
                )
