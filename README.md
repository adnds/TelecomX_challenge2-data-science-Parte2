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