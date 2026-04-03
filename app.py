import streamlit as st
import pandas as pd
import joblib

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(
    page_title="Previsão de Churn", 
    layout="wide",
    page_icon="📊"
)

# ==============================
# CARREGAR MODELO
# ==============================
model = joblib.load("model.pkl")  # Certifique-se de que o modelo esteja treinado com mesmas features

# ==============================
# TÍTULO E DESCRIÇÃO
# ==============================
st.title("📊 Previsão de Churn de Clientes")
st.markdown(
    """
    Este aplicativo permite prever a **probabilidade de churn** de um cliente utilizando modelos de Machine Learning.
    Insira os dados do cliente na barra lateral e clique em **Prever Churn**.
    """
)

# ==============================
# SIDEBAR PARA INPUTS
# ==============================
st.sidebar.header("📥 Dados do Cliente")

# Informações pessoais
gender = st.sidebar.selectbox("Gênero", ["Male", "Female"])
senior = st.sidebar.selectbox("Idoso?", [0, 1])
partner = st.sidebar.selectbox("Possui parceiro?", ["Yes", "No"])
dependents = st.sidebar.selectbox("Possui dependentes?", ["Yes", "No"])

# Contrato e tempo
tenure = st.sidebar.slider("Meses como cliente", 0, 72, 12)
contract = st.sidebar.selectbox("Contrato", ["Month-to-month", "One year", "Two year"])
paperless = st.sidebar.selectbox("Fatura digital", ["Yes", "No"])
payment = st.sidebar.selectbox("Forma de pagamento", [
    "Electronic check", "Mailed check", "Bank transfer", "Credit card"
])

# Serviços
phone_service = st.sidebar.selectbox("Telefone", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Múltiplas linhas", ["Yes", "No", "No phone service"])
internet_service = st.sidebar.selectbox("Internet", ["DSL", "Fiber optic", "No"])

# Valores
monthly = st.sidebar.number_input("Valor mensal", 0.0, 500.0, 70.0, step=1.0)
total = st.sidebar.number_input("Total gasto", 0.0, 20000.0, 1000.0, step=10.0)

# ==============================
# FEATURE ENGINEERING
# ==============================
avg_monthly_spend = total / (tenure + 1)
cliente_novo = 1 if tenure < 12 else 0

# ==============================
# CRIAR DATAFRAME
# ==============================
data = pd.DataFrame({
    "customer.gender": [gender],
    "customer.SeniorCitizen": [senior],
    "customer.Partner": [partner],
    "customer.Dependents": [dependents],
    "customer.tenure": [tenure],
    "phone.PhoneService": [phone_service],
    "phone.MultipleLines": [multiple_lines],
    "internet.InternetService": [internet_service],
    "account.Contract": [contract],
    "account.PaperlessBilling": [paperless],
    "account.PaymentMethod": [payment],
    "account.Charges.Monthly": [monthly],
    "account.Charges.Total": [total],
    "avg_monthly_spend": [avg_monthly_spend],
    "cliente_novo": [cliente_novo]
})

# ==============================
# PREDIÇÃO
# ==============================
if st.button("🔍 Prever Churn"):
    # Realizar previsão
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.subheader("Resultado da Previsão")
    
    # Exibir alerta de risco
    if prediction == 1:
        st.error(f"⚠️ Cliente com **ALTO risco de churn** ({probability:.2%})")
    else:
        st.success(f"✅ Cliente com **BAIXO risco de churn** ({probability:.2%})")
    
    # Mostrar barra de progresso
    st.progress(int(probability * 100))

# ==============================
# INFORMAÇÕES ADICIONAIS
# ==============================
st.markdown("---")
st.markdown(
    """
    Projeto de **Machine Learning para previsão de churn**.
    Este aplicativo foi desenvolvido como parte do desafio **Telecom X – Parte 2**.
    """
)