import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import GradientBoostingClassifier
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
# LOAD OU TREINA MODELO
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

    # ==============================
    # 1. TENTAR CARREGAR MODELO
    # ==============================
    if os.path.exists("model.pkl"):
        model, feature_cols = joblib.load("model.pkl")
        return model, feature_cols, COLS

    # ==============================
    # 2. TREINAR MODELO
    # ==============================
    if not os.path.exists("dados_tratados.csv"):
        raise FileNotFoundError("dados_tratados.csv não encontrado")

    df = pd.read_csv("dados_tratados.csv")
    df = df.dropna(subset=["Churn"])

    df["avg_monthly_spend"] = df[COLS["total"]] / (df[COLS["tenure"]] + 1)
    df["cliente_novo"] = (df[COLS["tenure"]] < 12).astype(int)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    X = pd.get_dummies(X, drop_first=True)

    model = GradientBoostingClassifier(random_state=42)
    model.fit(X, y)

    # salvar modelo
    joblib.dump((model, X.columns.tolist()), "model.pkl")

    return model, X.columns.tolist(), COLS


# ==============================
# CARREGAR
# ==============================
try:
    model, feature_cols, COLS = load_model()
except Exception as e:
    st.error(f"Erro ao carregar modelo: {e}")
    st.stop()

# ==============================
# UI
# ==============================
st.title("🚀 Previsor de Rotatividade de Cliente ")
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

input_encoded = pd.get_dummies(input_df, drop_first=True)
input_encoded = input_encoded.reindex(columns=feature_cols, fill_value=0)
input_encoded = input_encoded.apply(pd.to_numeric, errors="coerce").fillna(0)

# ==============================
# EXECUTAR
# ==============================
if st.button("🚀 Analisar Cliente"):

    prob = model.predict_proba(input_encoded)[0][1]

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