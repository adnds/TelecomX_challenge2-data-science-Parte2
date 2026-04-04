import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
import os

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="Previsor de Rotatividade de Clientes",
    layout="wide",
    page_icon="🚀"
)

# ==============================
# CSS
# ==============================
st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 2.2rem;
    font-weight: bold;
    color: #00d4ff;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #00d4ff;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOAD MODEL (APENAS INFERÊNCIA)
# ==============================
@st.cache_resource
def load_model():

    COLS = {
        "tenure": "customer.tenure",
        "monthly": "account.Charges.Monthly",
        "total": "account.Charges.Total",
        "gender": "customer.gender",
        "senior": "customer.SeniorCitizen",
        "partner": "customer.Partner",
        "dependents": "customer.Dependents",
        "phone": "phone.PhoneService",
        "multiple": "phone.MultipleLines",
        "internet": "internet.InternetService",
        "contract": "account.Contract",
        "paperless": "account.PaperlessBilling",
        "payment": "account.PaymentMethod",
    }

    if not os.path.exists("model.pkl"):
        st.error("❌ Modelo não encontrado. Faça upload do model.pkl no repositório.")
        st.stop()

    model, feature_cols = joblib.load("model.pkl")

    return model, feature_cols, COLS


# ==============================
# CARREGAR MODELO
# ==============================
try:
    model, feature_cols, COLS = load_model()
except Exception as e:
    st.error(f"Erro ao carregar modelo: {e}")
    st.stop()

# ==============================
# UI
# ==============================
st.title("🚀 Previsor de Rotatividade de Cliente")
st.caption("Sistema inteligente de previsão de churn")

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.header("📥 Dados do Cliente")

    gender = st.selectbox("Gênero", ["Male", "Female"])
    senior = st.selectbox("Idoso", [0, 1])
    partner = st.selectbox("Parceiro", ["Yes", "No"])
    dependents = st.selectbox("Dependentes", ["Yes", "No"])

    tenure = st.slider("Tempo (meses)", 0, 72, 12)

    contract = st.selectbox("Contrato", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Fatura digital", ["Yes", "No"])
    payment = st.selectbox("Pagamento", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

    phone = st.selectbox("Telefone", ["Yes", "No"])
    multiple = st.selectbox("Múltiplas linhas", ["Yes", "No", "No phone service"])
    internet = st.selectbox("Internet", ["DSL", "Fiber optic", "No"])

    monthly = st.number_input("Mensalidade", 0.0, 500.0, 70.0)
    total = st.number_input("Total gasto", 0.0, 20000.0, 1000.0)

# ==============================
# INPUT
# ==============================
input_dict = {
    COLS["gender"]: [gender],
    COLS["senior"]: [senior],
    COLS["partner"]: [partner],
    COLS["dependents"]: [dependents],
    COLS["tenure"]: [tenure],
    COLS["phone"]: [phone],
    COLS["multiple"]: [multiple],
    COLS["internet"]: [internet],
    COLS["contract"]: [contract],
    COLS["paperless"]: [paperless],
    COLS["payment"]: [payment],
    COLS["monthly"]: [monthly],
    COLS["total"]: [total],
    "avg_monthly_spend": [total / (tenure + 1)],
    "cliente_novo": [1 if tenure < 12 else 0],
}

input_df = pd.DataFrame(input_dict)

# ==============================
# ENCODING ROBUSTO
# ==============================
input_encoded = pd.get_dummies(input_df, drop_first=True)

# garantir mesmas colunas do treino
for col in feature_cols:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

input_encoded = input_encoded[feature_cols]
input_encoded = input_encoded.apply(pd.to_numeric, errors="coerce").fillna(0)

# ==============================
# EXECUTAR
# ==============================
if st.button("🚀 Analisar Cliente"):

    try:
        prob = model.predict_proba(input_encoded)[0][1]
    except Exception as e:
        st.error(f"Erro na previsão: {e}")
        st.stop()

    col1, col2, col3 = st.columns(3)

    col1.metric("Risco de Churn", f"{prob:.2%}")

    status = (
        "🔴 Crítico" if prob > 0.7
        else "🟡 Atenção" if prob > 0.4
        else "🟢 Saudável"
    )
    col2.metric("Status", status)

    col3.metric("Tempo", f"{tenure} meses")

    st.markdown("---")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={"text": "Probabilidade (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))

    st.plotly_chart(fig, use_container_width=True)

    # recomendações
    if prob > 0.7:
        st.error("🚨 Cliente com alto risco. Ação imediata recomendada.")
    elif prob > 0.4:
        st.warning("⚠️ Cliente em zona de atenção.")
    else:
        st.success("✅ Cliente estável.")