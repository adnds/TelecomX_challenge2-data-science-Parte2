# 📊 Telecom X – Previsão de Churn de Clientes

## 📌 Descrição do Projeto

Este projeto tem como objetivo desenvolver **modelos preditivos capazes de identificar clientes com maior probabilidade de cancelar os serviços da Telecom X (Churn)**.

A análise utiliza técnicas de **pré-processamento de dados, análise exploratória e Machine Learning** para identificar padrões associados à evasão de clientes e gerar insights estratégicos para retenção.

O projeto foi desenvolvido como parte do desafio **Telecom X – Parte 2: Prevendo Churn**.

---

## 🎯 Objetivos

O projeto busca:

- Preparar os dados para modelagem
- Identificar padrões relacionados ao churn
- Treinar modelos de Machine Learning
- Avaliar o desempenho dos modelos
- Interpretar as variáveis mais importantes
- Gerar insights estratégicos para retenção de clientes

---

## 🧠 Etapas do Projeto

### 1️⃣ Preparação dos Dados

O dataset foi carregado a partir do arquivo tratado na Parte 1 do desafio.

**Etapas realizadas:**

- Remoção de registros com Churn vazio
- Conversão da variável `Churn` para formato numérico
- Remoção da coluna `customerID` (identificador irrelevante)
- Criação de novas variáveis para enriquecer o modelo

#### 🔹 Novas Features Criadas

| Feature            | Descrição                                              |
|--------------------|--------------------------------------------------------|
| `avg_monthly_spend` | Estimativa de gasto médio mensal do cliente           |
| `cliente_novo`      | Identifica clientes com menos de 12 meses de contrato |

Essas variáveis ajudam o modelo a capturar padrões relacionados ao comportamento de cancelamento.

---

### 2️⃣ Encoding de Variáveis Categóricas

Para permitir o uso dos dados em algoritmos de Machine Learning, foi aplicado **One-Hot Encoding** utilizando:
```python
pd.get_dummies(drop_first=True)
```

---

### 3️⃣ Análise de Distribuição do Churn

- A maioria dos clientes permanece na empresa
- Existe desbalanceamento entre as classes, importante para a modelagem

Para lidar com isso, foi utilizado o parâmetro:
```python
class_weight="balanced"
```

---

### 📊 Análise de Correlação

Foi construída uma matriz de correlação para identificar variáveis relacionadas ao churn.

**Principais variáveis associadas ao cancelamento:**

- Clientes novos (`cliente_novo`)
- Internet por fibra
- Pagamento via Electronic Check
- Valor mensal elevado
- Baixo tempo de contrato

> Essas variáveis são fortes indicadoras de risco de evasão.

---

## 🤖 Modelagem Preditiva

O dataset foi dividido em:

- **70%** treino
- **30%** teste
```python
train_test_split(test_size=0.3, random_state=42)
```

Foram testados três modelos de classificação:

| Modelo               | Tipo                      |
|----------------------|---------------------------|
| Logistic Regression  | Modelo linear             |
| Random Forest        | Ensemble baseado em árvores |
| Gradient Boosting    | Ensemble sequencial       |

### ⚙️ Normalização dos Dados

- **StandardScaler** aplicado para modelos sensíveis à escala (Logistic Regression)
- Modelos baseados em árvores **não necessitam** normalização (Random Forest, Gradient Boosting)

---

## 📈 Avaliação dos Modelos

**Métricas utilizadas:**

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de Confusão

Essas métricas permitem avaliar tanto a precisão geral quanto a capacidade de identificar clientes que realmente cancelam.

### 📊 Comparação dos Modelos

| Modelo              | Accuracy | Precision | Recall | F1-score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | ~0.73    | ~0.50     | ~0.79  | ~0.61    |
| Random Forest       | ~0.76    | ~0.55     | ~0.69  | ~0.61    |
| Gradient Boosting   | ~0.78    | ~0.63     | ~0.56  | ~0.59    |

### 📌 Interpretação

- **Gradient Boosting** apresentou a maior acurácia
- **Logistic Regression** apresentou melhor recall
- **Random Forest** apresentou melhor equilíbrio geral

> O melhor modelo depende do objetivo do negócio. Para estratégias de retenção, **recall geralmente é mais importante**, pois prioriza identificar o maior número possível de clientes que irão cancelar.

---

## 🔎 Importância das Variáveis

Utilizando o modelo **Random Forest**, foram identificadas as variáveis mais importantes:

1. Tempo de contrato (`tenure`)
2. Valor mensal (`Charges.Monthly`)
3. Tipo de contrato
4. Forma de pagamento
5. Tipo de internet
6. Gasto médio mensal (`avg_monthly_spend`)

---

## 📊 Visualizações Utilizadas

- Distribuição de churn
- Matriz de correlação
- Matrizes de confusão
- Gráfico de importância das variáveis

---

## 📌 Conclusões Estratégicas

**Principais insights:**

- Clientes novos têm maior probabilidade de churn
- Clientes com contratos mensais cancelam mais
- Pagamentos via Electronic Check estão associados a maior churn
- Clientes com internet fibra apresentam maior evasão

### 🚀 Possíveis Estratégias para Redução de Churn

- Criar programas de retenção para clientes novos
- Incentivar contratos de longo prazo
- Oferecer benefícios para clientes com alto gasto mensal
- Monitorar clientes com alto risco preditivo de churn

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📂 Estrutura do Projeto

telecomx-churn-analysis/
│
├── dados_tratados.csv
├── TelecomX_Churn_Analysis.ipynb
└── README.md

---

## 👨‍💻 Autor

Adilson Nascimento

Projeto desenvolvido para o desafio de Data Science – Telecom X.

---

## 📎 Observação

> Este projeto tem finalidade educacional e analítica, demonstrando a aplicação de técnicas de Machine Learning para previsão de churn de clientes.
=======
#  Telecom X – Previsão de Churn de Clientes

##  Descrição do Projeto

Este projeto tem como objetivo desenvolver **modelos preditivos capazes de identificar clientes com maior probabilidade de cancelar os serviços da Telecom X (Churn)**.

A análise utiliza técnicas de **pré-processamento de dados, análise exploratória e Machine Learning** para identificar padrões associados à evasão de clientes e gerar **insights estratégicos para retenção**.

O projeto foi desenvolvido como parte do desafio **Telecom X – Parte 2: Prevendo Churn**.

---

#  Objetivos

O projeto busca:

- Preparar os dados para modelagem
- Identificar padrões relacionados ao churn
- Treinar modelos de Machine Learning
- Avaliar o desempenho dos modelos
- Interpretar as variáveis mais importantes
- Gerar **insights estratégicos para retenção de clientes**

---

#  Etapas do Projeto

## 1️⃣ Preparação dos Dados

Inicialmente foi carregado o dataset previamente tratado na **Parte 1 do desafio**.

Etapas realizadas:

- Remoção de registros com `Churn` vazio
- Conversão da variável `Churn` para formato numérico
- Remoção da coluna `customerID` (identificador irrelevante)
- Criação de novas variáveis para enriquecer o modelo

### 🔹 Novas Features Criadas

| Feature | Descrição |
|------|------|
| `avg_monthly_spend` | Estimativa de gasto médio mensal do cliente |
| `cliente_novo` | Identifica clientes com menos de 12 meses de contrato |

Essas variáveis ajudam o modelo a capturar padrões relacionados ao comportamento de cancelamento.

---

## 2️⃣ Encoding de Variáveis Categóricas

Para permitir o uso dos dados em algoritmos de Machine Learning, foi aplicado **One-Hot Encoding** utilizando:

```python
pd.get_dummies(drop_first=True)
```

Esse processo transforma variáveis categóricas em variáveis numéricas.

O parâmetro `drop_first=True` foi utilizado para evitar **multicolinearidade**.

---

## 3️⃣ Análise de Distribuição do Churn

Foi analisada a proporção de clientes que cancelaram o serviço.

Observação:

- A maioria dos clientes **permanece na empresa**
- Existe **desbalanceamento entre as classes**

Esse fator é importante pois pode influenciar os modelos de Machine Learning.

Para lidar com isso foi utilizado:

```python
class_weight="balanced"
```

nos modelos.

---

#  Análise de Correlação

Foi construída uma **matriz de correlação** para identificar variáveis relacionadas ao churn.

Principais variáveis associadas ao cancelamento:

- Clientes novos (`cliente_novo`)
- Internet por **fibra**
- Pagamento via **Electronic Check**
- **Valor mensal elevado**
- Baixo tempo de contrato

Essas variáveis são fortes indicadoras de risco de evasão.

---

#  Modelagem Preditiva

O dataset foi dividido em:

- **70% treino**
- **30% teste**

```python
train_test_split(test_size=0.3, random_state=42)
```

Foram testados **três modelos de classificação**:

| Modelo | Tipo |
|------|------|
| Logistic Regression | Modelo linear |
| Random Forest | Ensemble baseado em árvores |
| Gradient Boosting | Ensemble sequencial |

---

# ⚙️ Normalização dos Dados

Foi aplicada **padronização com StandardScaler** para modelos sensíveis à escala.

Modelos que utilizam normalização:

- Logistic Regression

Modelos baseados em árvores **não necessitam normalização**:

- Random Forest  
- Gradient Boosting

---

# 📈 Avaliação dos Modelos

Os modelos foram avaliados utilizando as seguintes métricas:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Matriz de Confusão**

Essas métricas permitem avaliar tanto a **precisão geral** quanto a **capacidade de identificar clientes que realmente cancelam**.

---

#  Comparação dos Modelos

| Modelo | Accuracy | Precision | Recall | F1-score |
|------|------|------|------|------|
| Logistic Regression | ~0.73 | ~0.50 | ~0.79 | ~0.61 |
| Random Forest | ~0.76 | ~0.55 | ~0.69 | ~0.61 |
| Gradient Boosting | ~0.78 | ~0.63 | ~0.56 | ~0.59 |

###  Interpretação

- **Gradient Boosting apresentou a maior acurácia**
- **Logistic Regression apresentou melhor recall**
- **Random Forest apresentou melhor equilíbrio geral**

O melhor modelo depende do objetivo do negócio:

- **Maximizar recall:** identificar mais clientes que irão cancelar
- **Maximizar precisão:** reduzir alertas falsos

Para estratégias de retenção, geralmente **recall é mais importante**.

---

#  Importância das Variáveis

Utilizando o modelo **Random Forest**, foram identificadas as variáveis mais importantes para prever churn.

Principais fatores associados ao cancelamento:

- Tempo de contrato (`tenure`)
- Valor mensal (`Charges.Monthly`)
- Tipo de contrato
- Forma de pagamento
- Tipo de internet
- Gasto médio mensal

Essas variáveis indicam **comportamento e perfil de risco do cliente**.

---

#  Visualizações Utilizadas

Durante a análise foram utilizados:

- Distribuição de churn
- Matriz de correlação
- Matrizes de confusão
- Gráfico de importância das variáveis

Essas visualizações ajudam a entender **padrões e relações entre as variáveis**.

---

#  Conclusões Estratégicas

A análise mostrou que **o churn está fortemente associado a alguns fatores comportamentais e contratuais**.

Principais insights:

### 1️⃣ Clientes novos têm maior probabilidade de churn

Clientes com menos tempo de contrato apresentam maior risco de cancelamento.

### 2️⃣ Clientes com contratos mensais cancelam mais

Contratos de curto prazo indicam menor fidelização.

### 3️⃣ Pagamentos via Electronic Check estão associados a maior churn

Isso pode indicar menor comprometimento ou perfil de cliente mais propenso a cancelar.

### 4️⃣ Clientes com internet fibra apresentam maior evasão

Pode indicar insatisfação com preço ou qualidade do serviço.

---

#  Possíveis Estratégias para Redução de Churn

Com base na análise, a empresa pode:

- Criar **programas de retenção para clientes novos**
- Incentivar **contratos de longo prazo**
- Oferecer **benefícios para clientes com alto gasto mensal**
- Monitorar clientes com **alto risco preditivo de churn**

---

#  Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📂 Estrutura do Projeto

```
telecomx-churn-analysis
│
├── dados_tratados.csv
├── TelecomX_Churn_Analysis.ipynb
├── README.md
```

---

## 🚀 Deploy da Aplicação (Streamlit Cloud)

A aplicação interativa de previsão de churn foi disponibilizada online utilizando o **Streamlit Cloud**, permitindo simular cenários de clientes em tempo real.

---

## 🌐 Acesse a aplicação

👉 **Link do app:**  
https://SEU-LINK.streamlit.app  

---

## ⚙️ Como foi feito o deploy

O deploy foi realizado utilizando o serviço oficial do Streamlit:

- Repositório hospedado no GitHub  
- Arquivo principal: `app.py` (ou nome equivalente)  
- Modelo salvo com `joblib` (`model.pkl`)  
- Dataset tratado (`dados_tratados.csv`)  

---

## 📌 Passos principais

1. Subir o projeto para o GitHub  
2. Acessar: https://streamlit.io/cloud  
3. Conectar sua conta GitHub  
4. Selecionar o repositório  
5. Definir o arquivo principal (ex: `app.py`)  
6. Deploy automático 🚀  

---

#  Autor
Adilson Nascimento
Projeto desenvolvido para o desafio de **Data Science – Telecom X**.

---

# 📎 Observação

Este projeto tem finalidade **educacional e analítica**, demonstrando a aplicação de técnicas de **Machine Learning para previsão de churn de clientes**

---