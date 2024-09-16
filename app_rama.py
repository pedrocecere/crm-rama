import streamlit as st
from contrato_rama import Distribuicao
from datetime import datetime, time
from pydantic import ValidationError
from database_rama import salvar_no_postgres_rama

def main():

    st.set_page_config(
        page_title="Distribuições ONR",
        page_icon="📊",
        layout="wide",
    )
    
    # Adicionar logotipo da empresa
    st.image(r"C:\Users\pedro.cecere\Documents\Projetos\pipeline\crm-rama\AF_RAMA ADVOGADOS_HORIZONTAL_ 2_COLOR_sem associados.png", width=500)

    st.title("Distribuições ONR")
    data_af_07 = st.date_input("Data AF 0.7", datetime.now())
    data_af_11 = st.date_input("Data AF 1.1", datetime.now())
    data_distribuicao = st.date_input("Data da Distribuição", datetime.now())
    codigo = codigo = st.text_input("Código").upper()
    dossie = st.text_input("Dossiê")
    mutuario = st.text_input("Nome do Mutuário").title()
    produto = st.selectbox("Produto", options=["Home Equity PJ", "Home Equity PF", "Financiamento", "Hipoteca"])
    responsavel = st.selectbox("Responsável", options=["Darlei", "Sarah", "João Lucas", "Maira"])
    if st.button("Salvar"):
        try:
            
            venda = Distribuicao(
                data_af_07 = data_af_07,
                data_af_11 = data_af_11,
                data_distribuicao = data_distribuicao,
                codigo = codigo,
                dossie = dossie,
                mutuario = mutuario,
                responsavel = responsavel,
                produto = produto
            )
            st.write(venda)
            salvar_no_postgres_rama(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__=="__main__":
    main()