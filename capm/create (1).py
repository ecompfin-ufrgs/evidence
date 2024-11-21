"""
Função Cria Base de Dados para Modelo CAPM
Essa função cria (ou acessa) uma base de dados a qual contém uma tabela que armazena os preços históricos, os retornos do mercado, as taxas livre de risco e os retornos calculados dos ativos.
Autores: Murilo Fiorio Pires e Vitor Netto
Data: 19/11/2024
Versão: 0.0.1
"""

import sqlite3

def create():
    # Conectar ou criar o banco de dados
    conn = sqlite3.connect("capm_database.db")
    cursor = conn.cursor()

    # Criar tabela para armazenar preços históricos dos ativos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asset_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_symbol TEXT NOT NULL,
            date DATE NOT NULL,
            closing_price REAL NOT NULL,
            UNIQUE(asset_symbol, date)
        )
    ''')

    # Criar tabela para armazenar os retornos do mercado
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market_returns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            market_return REAL NOT NULL,
            UNIQUE(date)
        )
    ''')

    # Criar tabela para armazenar a taxa livre de risco
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS risk_free_rate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            rate REAL NOT NULL,
            UNIQUE(date)
        )
    ''')

    # Criar tabela para armazenar retornos calculados dos ativos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asset_returns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_symbol TEXT NOT NULL,
            date DATE NOT NULL,
            return REAL NOT NULL,
            UNIQUE(asset_symbol, date)
        )
    ''')

    # Confirmar alterações e fechar conexão
    conn.commit()
    conn.close()