import sqlite3
import os
import hashlib
from datetime import datetime, timedelta
from .planos import PLANOS

def init_db():
    conn = sqlite3.connect('api_keys.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_keys (
            key_hash TEXT PRIMARY KEY,
            email TEXT,
            plano TEXT DEFAULT 'gratis',
            chamadas_mes INTEGER DEFAULT 0,
            chamadas_total INTEGER DEFAULT 0,
            mes_reset TEXT,
            origem TEXT DEFAULT 'site',
            data_criacao TEXT,
            ultimo_uso TEXT
        )
    ''')
    conn.commit()
    conn.close()

def gerar_api_key(email: str) -> str:
    raw = f"{email}:{os.urandom(16).hex()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:32]

def verificar_api_key(api_key: str, db_path: str = 'api_keys.db'):
    """Verifica API Key e aplica limite de plano (só para chaves do site)"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT plano, chamadas_mes, mes_reset, origem FROM api_keys WHERE key_hash = ?',
        (api_key,)
    )
    resultado = cursor.fetchone()
    
    if not resultado:
        conn.close()
        return {"valido": False, "erro": "API Key inválida"}
    
    plano, chamadas_mes, mes_reset, origem = resultado
    
    # Se a chave veio do RapidAPI, não aplicamos limite
    if origem == 'rapidapi':
        conn.close()
        return {
            "valido": True,
            "plano": plano,
            "nome_plano": "RapidAPI",
            "chamadas_usadas": 0,
            "limite": "Ilimitado (gerido pelo RapidAPI)",
            "restantes": "Ilimitado"
        }
    
    # Para chaves do site, aplicar limite mensal
    agora = datetime.now()
    mes_atual = agora.strftime('%Y-%m')
    
    if mes_reset != mes_atual:
        chamadas_mes = 0
        mes_reset = mes_atual
    
    
    info_plano = PLANOS.get(plano, PLANOS['gratis'])
    limite = info_plano['chamadas_mes']
    
    if chamadas_mes >= limite:
        conn.close()
        return {
            "valido": False,
            "erro": f"Limite do plano {info_plano['nome']} atingido ({limite} chamadas/mês). Faça upgrade."
        }
    

    cursor.execute(
        '''UPDATE api_keys 
           SET chamadas_mes = chamadas_mes + 1, 
               chamadas_total = chamadas_total + 1,
               mes_reset = ?,
               ultimo_uso = ?
           WHERE key_hash = ?''',
        (mes_atual, agora.isoformat(), api_key)
    )
    conn.commit()
    conn.close()
    
    return {
        "valido": True,
        "plano": plano,
        "nome_plano": info_plano['nome'],
        "chamadas_usadas": chamadas_mes + 1,
        "limite": limite,
        "restantes": limite - (chamadas_mes + 1)
    }

def obter_info_chave(api_key: str, db_path: str = 'api_keys.db'):
    """Retorna info da chave sem incrementar contador"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT plano, chamadas_mes, mes_reset, origem FROM api_keys WHERE key_hash = ?',
        (api_key,)
    )
    resultado = cursor.fetchone()
    conn.close()
    
    if not resultado:
        return None
    
    plano, chamadas_mes, mes_reset, origem = resultado
    info_plano = PLANOS.get(plano, PLANOS['gratis'])
    
    return {
        "plano": plano,
        "nome_plano": info_plano['nome'],
        "chamadas_usadas": chamadas_mes,
        "limite": info_plano['chamadas_mes'],
        "restantes": info_plano['chamadas_mes'] - chamadas_mes,
        "origem": origem
    }