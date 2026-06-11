import json
import os
from datetime import datetime

LOG_FILE = "api_logs.json"

def registrar_log(api_key_hash: str, plano: str, endpoint: str, ip: str, numero: str, sucesso: bool, detalhes: str = ""):
    """Regista uma chamada à API no ficheiro de log"""
    
    entrada = {
        "data": datetime.now().isoformat(),
        "api_key": api_key_hash[:8] + "...",  # só mostramos parte da chave
        "plano": plano,
        "endpoint": endpoint,
        "ip": ip,
        "numero": numero[:10] + "..." if len(numero) > 10 else numero,  # truncar número
        "sucesso": sucesso,
        "detalhes": detalhes
    }
    
    # Carregar logs existentes
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    
    # Adicionar nova entrada
    logs.append(entrada)
    
    # Manter só os últimos 1000 registos
    if len(logs) > 1000:
        logs = logs[-1000:]
    
    # Guardar
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def obter_logs(limite: int = 50):
    """Retorna os últimos logs"""
    if not os.path.exists(LOG_FILE):
        return []
    
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    return logs[-limite:]

def obter_estatisticas():
    """Retorna estatísticas básicas de uso"""
    if not os.path.exists(LOG_FILE):
        return {"total_chamadas": 0, "por_plano": {}, "ultima_hora": 0}
    
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    agora = datetime.now()
    
    # Chamadas por plano
    por_plano = {}
    ultima_hora = 0
    
    for log in logs:
        plano = log.get("plano", "desconhecido")
        por_plano[plano] = por_plano.get(plano, 0) + 1
        
        # Verificar se foi na última hora
        try:
            data_log = datetime.fromisoformat(log["data"])
            if (agora - data_log).total_seconds() < 3600:
                ultima_hora += 1
        except:
            pass
    
    return {
        "total_chamadas": len(logs),
        "por_plano": por_plano,
        "ultima_hora": ultima_hora
    }