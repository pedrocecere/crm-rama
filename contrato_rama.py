from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Home Equity PJ"
    produto2 = "Home Equity PF"
    produto3 = "Financiamento"
    produto4 = "Hipoteca"

class ResponsavelEnum(str, Enum):
    produto1 = "Darlei"
    produto2 = "Sarah"
    produto3 = "João Lucas"
    produto4 = "Maira"

class Distribuicao(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        data_af_07 (datetime): Data de AF 0.7.
        data_af_11 (datetime): Data de AF 1.1.
        data_distribuicao (datetime): Data da distribuição.
        codigo (str): Código de identificação.
        dossie (str): Número do dossiê.
        mutuario (str): Nome do mutuário.
        responsavel (ResponsavelEnum): Responsável pelo processo.
        produto (ProdutoEnum): Categoria do produto.
    """

    data_af_07 : datetime
    data_af_11 : datetime
    data_distribuicao : datetime
    codigo : str
    dossie : str
    mutuario : str 
    responsavel : ResponsavelEnum
    produto : ProdutoEnum
