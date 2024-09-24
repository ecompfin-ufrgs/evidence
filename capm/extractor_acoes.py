import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime

"""
Função Extrai Dados de Ações da B3
Essa função coleta preços de fechamento de uma ação da B3 no Yahoo Finance para uma lista de datas específicas e os retorna em forma de lista
Autores: Gabriel Pegoraro Vieira, Murilo Fiorio Pires
Data: 24/09/2024
Versão: 0.0.1
"""

def get_stock_price_b3(codigo: str, datas: list) -> list:
   """Esta função coleta dados de ações da B3 no Yahoo Finance.  Seus argumentos
   são o código da ação e uma lista com datas desejadas"""
   
   ticker = f"{codigo}.SA"
   
   # Baixa os dados históricos entre o menor e o maior intervalo de data fornecidos
   dados = yf.download(ticker, start=min(datas), end=max(datas))
   
   # Converte data de string para objeto datetime
   datas_convertidas = list(map(lambda data: datetime.strptime(data, '%Y-%m-%d'), datas))
   
   # Função que busca o preço de fechamento em um data específica
   def buscar_preco(data):
      return dados.loc[dados.index == data]['Close'].values[0] if not dados.loc[dados.index == data].empty else None
   
   # Aplica a função buscar_preco para todas as datas convertidas
   precos = list(map(buscar_preco, datas_convertidas))

   return precos
