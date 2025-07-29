import streamlit as st
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os 

# Carregar variáveis do .env
load_dotenv()

# Ler variáveis de ambiente
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
st.title("🧪 Teste de conexão e codificação com PostgreSQL")

# 🔌 Conexão com PostgreSQL (sem LLM por enquanto)
@st.cache_resource
def connect_db():
    DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return psycopg2.connect(DB_URI, options="-c client_encoding=UTF8")

# Consulta fixa
sql = "SELECT * FROM clientes LIMIT 5"

try:
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    # Debug do conteúdo bruto
    st.write("🔎 Dados brutos (antes do DataFrame):")
    st.write(rows)

    # Cria DataFrame
    df = pd.DataFrame(rows, columns=columns)
    
    # Debug das colunas de texto
    for col in df.select_dtypes(include='object'):
        try:
            df[col] = df[col].apply(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)
        except Exception as e:
            st.warning(f"Erro na coluna '{col}': {e}")

    st.success("✅ Leitura realizada com sucesso!")
    st.dataframe(df)

except Exception as e:
    st.error(f"❌ Erro geral: {e}")
