import psycopg2
from psycopg2 import sql
from contrato_rama import Distribuicao
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres_rama(dados: Distribuicao):
    """
    Função para salvar no banco de dados PostgreSQL
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Inserção dos dados na tabela
        insert_query = sql.SQL(
            """
            INSERT INTO pipeline.distribuicao 
            (data_af_07, data_af_11, data_distribuicao, codigo, dossie, mutuario, responsavel, produto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        )
        
        # Execução da query
        cursor.execute(insert_query, (
            dados.data_af_07,
            dados.data_af_11,
            dados.data_distribuicao,
            dados.codigo,
            dados.dossie,
            dados.mutuario,
            dados.responsavel.value,  # O valor da Enum precisa ser acessado assim
            dados.produto.value       # O valor da Enum precisa ser acessado assim
        ))

        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")
