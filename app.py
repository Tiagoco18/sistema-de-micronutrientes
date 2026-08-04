import streamlit as st
import requests

st.title("Sistema de Micronutrientes")

try:
    url = st.secrets["url"]
    auth_token = st.secrets["auth_token"]
    
    # Converter libsql:// para https://
    url = url.replace("libsql://", "https://")
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(
        f"{url}/v1/query",
        json={"queries": [{"q": "SELECT 1 as teste"}]},
        headers=headers
    )
    if response.status_code == 200:
        st.success("Banco de dados conectado!")
    else:
        st.error(f"Erro na conexao: {response.text}")
except Exception as e:
    st.error(f"Erro: {e}")
