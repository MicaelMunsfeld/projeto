import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Configuração das colunas de seleção
cols = st.columns(3)
colunas = cols[0].multiselect(
    'Dimensões Coluna',
    st.session_state['dimensao'] + st.session_state['dimensao_tempo']
)
valor = cols[1].selectbox(
    'Medidas',
    st.session_state['medida']
)
cor = cols[2].selectbox(
    'Cor',
    colunas
)

# Tabs para diferentes tipos de gráficos
tabs = st.tabs(['Treemap', 'Sunburst', 'Sankey', 'TimeSeries'])

# Verificação se há colunas suficientes para o gráfico
if len(colunas) > 2:
    with tabs[0]:
        # Filtra o DataFrame para remover valores zero no campo 'valor' selecionado
        df_filtered = st.session_state['df'][st.session_state['df'][valor] > 0]
        
        # Verifica se o DataFrame filtrado não está vazio para evitar ZeroDivisionError
        if not df_filtered.empty:
            fig = px.treemap(
                df_filtered,
                path=colunas,
                values=valor,
                color=cor,
                height=800,
                width=1200
            )
            fig.update_traces(textinfo='label+value')
            st.plotly_chart(fig)
        else:
            st.warning("Não há dados suficientes para gerar o gráfico. Verifique os valores.")
    
    with tabs[1]:
        # Gráfico Sunburst (configuração similar ao Treemap)
        if not df_filtered.empty:
            fig = px.sunburst(
                df_filtered,
                path=colunas,
                values=valor,
                color=cor,
                height=800,
                width=1200
            )
            fig.update_traces(textinfo='label+value')
            st.plotly_chart(fig)
        else:
            st.warning("Não há dados suficientes para gerar o gráfico. Verifique os valores.")

# Outras tabs como Sankey e TimeSeries podem seguir lógica semelhante se estiverem enfrentando problemas semelhantes.
