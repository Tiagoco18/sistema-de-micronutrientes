import streamlit as st
import os
from libsql_client import create_client_sync

# Configurar cliente Turso
url = os.getenv("DATABASE_URL")
auth_token = os.getenv("DATABASE_AUTH_TOKEN")
client = create_client_sync(url=url, auth_tokens=auth_token)

st.title("Sistema de Micronutrientes")
st.write("Conectado ao banco de dados!")

# Teste de conexão
try:
    result = client.execute("SELECT 1")
    st.success("? Banco de dados conectado!")
except Exception as e:
    st.error(f"? Erro: {e}")
