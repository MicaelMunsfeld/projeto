import streamlit as st

st.title('Tabela')
st.dataframe(
    st.session_state['dif'],
    hide_index=True,
    use_container_width=True,
    column_config={
        'data': st.column_config.DateColumn(label='Data do Jogo'),
        'publico_max': st.column_config.NumberColumn(label='Público Máximo', format='%.0f')
    }
)
