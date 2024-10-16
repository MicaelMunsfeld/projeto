import streamlit as st 

st.title("Tabela de Dados")
st.dataframe(
    st.session_state['df'],
    hide_index=True,
    use_container_width=True,
    column_config={
        'data': st.column_config.DateColumn(label="Data"),
        'publico': st.column_config.NumberColumn(label="Público", format='RS %.2f'),
    }
)
