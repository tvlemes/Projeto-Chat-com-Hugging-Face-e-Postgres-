import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import psycopg2


# Carregar variáveis do .env
load_dotenv()

# Ler variáveis de ambiente
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Criar conexão com o banco
DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = psycopg2.connect(DB_URI, options="-c client_encoding=UTF8")


# Endpoint LM Studio local
HUGGINGFACE_LOCAL_ENDPOINT = "http://localhost:1234/v1/completions"

# Função para gerar SQL a partir de pergunta
def pergunta_para_sql(pergunta, schema_hint=""):
    prompt = f"""### Transforme linguagem natural em SQL PostgreSQL
Esquema: {schema_hint}
Pergunta: {pergunta}
SQL:"""

    payload = {
        "model": "sqlcoder",  # ou o nome do modelo carregado no LM Studio
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0,
    }

    response = requests.post(HUGGINGFACE_LOCAL_ENDPOINT, json=payload)
    sql = response.json()['choices'][0]['text'].strip()
    return sql

# Interface Streamlit
st.title("🔍 Consultas com Hugging Face + PostgreSQL")

pergunta = st.text_input("Pergunte algo sobre as vendas:")

if pergunta:
    schema_hint = (
        "Tabelas:\n"
        "produtos(id, nome, preco),\n"
        "clientes(id, nome, email),\n"
        "vendas(id, cliente_id, produto_id, quantidade, data)\n"
        "Relacionamentos:\n"
        "vendas.cliente_id → clientes.id\n"
        "vendas.produto_id → produtos.id"
    )

    try:
        sql = pergunta_para_sql(pergunta, schema_hint=schema_hint)
        st.code(sql, language="sql")

        df = pd.read_sql_query(sql, engine)
        st.dataframe(df)

        if len(df.columns) >= 2:
            col_x = st.selectbox("Coluna X", df.columns)
            col_y = st.selectbox("Coluna Y", df.columns)
            fig = px.bar(df, x=col_x, y=col_y)
            st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Não foi possível gerar a consulta.")
