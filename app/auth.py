import sqlite3
import os
import hashlib
from datetime import datetime

def init_db():
    conn = sqlite3.connect('api_keys.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_keys (
            key_hash TEXT PRIMARY KEY,
            plano TEXT DEFAULT 'gratis',
            chamadas_mes INTEGER DEFAULT 0,
            chamadas_total INTEGER DEFAULT 0,
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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT plano, chamadas_mes FROM api_keys WHERE key_hash = ?',
        (api_key,)
    )
    resultado = cursor.fetchone()
    
    if not resultado:
        conn.close()
        return None
    
    plano, chamadas_mes = resultado
    
    cursor.execute(
        '''UPDATE api_keys 
           SET chamadas_mes = chamadas_mes + 1, 
               chamadas_total = chamadas_total + 1, 
               ultimo_uso = ? 
           WHERE key_hash = ?''',
        (datetime.now().isoformat(), api_key)
    )
    conn.commit()
    conn.close()
    
    return {"plano": plano, "chamadas_mes": chamadas_mes + 1}