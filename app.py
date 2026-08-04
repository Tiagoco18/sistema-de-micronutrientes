import streamlit as st
import requests
import os

st.title("Sistema de Micronutrientes")

# Configurar conexão Turso
url = os.getenv("DATABASE_URL")
auth_token = os.getenv("DATABASE_AUTH_TOKEN")

if not url or not auth_token:
    st.error("? Secrets não configurados!")
else:
    try:
        # Teste de conexão
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.post(
            f"{url}/v2/query",
            json={"queries": [{"q": "SELECT 1 as teste"}]},
            headers=headers
        )
        if response.status_code == 200:
            st.success("? Banco de dados conectado!")
        else:
            st.error(f"? Erro na conexão: {response.text}")
    except Exception as e:
        st.error(f"? Erro: {e}")
