import streamlit as st
from libsql_client import create_client

st.title("Sistema de Micronutrientes")

try:
    url = st.secrets["url"]
    auth_token = st.secrets["auth_token"]
    
    client = create_client(url=url, auth_token=auth_token)
    result = client.execute("SELECT 1 as teste")
    
    st.success("Banco de dados conectado!")
    st.write(result)
except Exception as e:
    st.error(f"Erro: {e}")
