"""Função Extractor_cdi
Descrição: Essa função retira os valores do cdi em uma dado periodo(inicial,final),
caso o usuário não coloque o periodo final é utilizado a observação mais recente.
Autores: Alexandre Araujo,Vitor de Almeida Netto
Data: 20/09/24 
versão: 0.0.1
"""


from bcb import sgs
import pandas as pd
from datetime import datetime, date


def get_cdi(inicial: datetime, final=None):
    if final is None:
        cdi = sgs.get({'cdi':12}, start = inicial)
        return cdi
    else:
        cdi = sgs.get({'cdi':12}, start = inicial, end=final)
        return cdi

