import streamlit as st
from app.consumo_api import resposta

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = resposta.json()
    st.success("Painel atualizado.")

    st.subheader("Indicadores principais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Latitude",
        f"{dados['latitude']:.2f}")
    col2.metric(
        "Longitude",
        f"{dados['longitude']:.2f}")
    col3.metric(
        "temperatura",
        f"{dados['current']['temperature_2m']:.1f}°C")
    
except Exception as erro:
    st.error(f"Erro ao atualizar o painel: {erro}")