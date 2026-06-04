from fastapi import FastAPI, HTTPException, Query, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from typing import Optional
import time 
from datetime import datetime, timedelta
from collections import defaultdict
from fastapi import FastAPI, HTTPException, Query, Security, Request

from .validators import (
        MozambiquePhoneValidator,
        AngolaPhoneValidator,
        BrazilPhoneValidator,
        PortugalPhoneValidator,
        ItalyPhoneValidator,
        CapeVerdePhoneValidator,
        GuineaBissauPhoneValidator,
        SaoTomePhoneValidator,
        EastTimorPhoneValidator,
        SouthAfricaPhoneValidator,
        NigeriaPhoneValidator,
        KenyaPhoneValidator,
        TanzaniaPhoneValidator,
        GhanaPhoneValidator,
        EthiopiaPhoneValidator,
        ZimbabwePhoneValidator,
        ZambiaPhoneValidator,
        EgyptPhoneValidator,
        MoroccoPhoneValidator,
        AlgeriaPhoneValidator,
        UgandaPhoneValidator,
        IvoryCoastPhoneValidator,
        SenegalPhoneValidator,
        CameroonPhoneValidator,
        RwandaPhoneValidator,
        InternacionalPhoneValidator
    )
from .models import PhoneNumberRequest, PhoneNumberResponse, RegistroRequest
from .auth import init_db, gerar_api_key, verificar_api_key
from .planos import PLANOS

app = FastAPI(
    title="Phone Validator API",
    description="API de validação de números de telefone africanos e internacionais",
    version="1.0.0"
)
# Controlo de demonstração por IP
demo_usage = defaultdict(list)
DEMO_LIMIT = 5  # chamadas por hora
DEMO_WINDOW = timedelta(hours=1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

VALIDATORS = {
        '258': MozambiquePhoneValidator(),
        '244': AngolaPhoneValidator(),
        '55': BrazilPhoneValidator(),
        '351': PortugalPhoneValidator(),
        '39': ItalyPhoneValidator(),
        '238': CapeVerdePhoneValidator(),
        '245': GuineaBissauPhoneValidator(),
        '239': SaoTomePhoneValidator(),
        '670': EastTimorPhoneValidator(),
        '27': SouthAfricaPhoneValidator(),
        '234': NigeriaPhoneValidator(),
        '254': KenyaPhoneValidator(),
        '255': TanzaniaPhoneValidator(),
        '233': GhanaPhoneValidator(),
        '251': EthiopiaPhoneValidator(),
        '263': ZimbabwePhoneValidator(),
        '260': ZambiaPhoneValidator(),
        '20': EgyptPhoneValidator(),
        '212': MoroccoPhoneValidator(),
        '213': AlgeriaPhoneValidator(),
        '256': UgandaPhoneValidator(),
        '225': IvoryCoastPhoneValidator(),
        '221': SenegalPhoneValidator(),
        '237': CameroonPhoneValidator(),
        '250': RwandaPhoneValidator(),
    }

PAIS_POR_CODIGO = {
    '+258': ('258', 'Moçambique'),
    '+244': ('244', 'Angola'),
    '+55': ('55', 'Brasil'),
    '+351': ('351', 'Portugal'),
    '+39': ('39', 'Itália'),
    '+238': ('238', 'Cabo Verde'),
    '+245': ('245', 'Guiné-Bissau'),
    '+239': ('239', 'São Tomé e Príncipe'),
    '+670': ('670', 'Timor-Leste'),
    '+27': ('27', 'África do Sul'),
    '+234': ('234', 'Nigéria'),
    '+254': ('254', 'Quénia'),
    '+255': ('255', 'Tanzânia'),
    '+233': ('233', 'Gana'),
    '+251': ('251', 'Etiópia'),
    '+263': ('263', 'Zimbabué'),
    '+260': ('260', 'Zâmbia'),
    '+20': ('20', 'Egito'),
    '+212': ('212', 'Marrocos'),
    '+213': ('213', 'Argélia'),
    '+256': ('256', 'Uganda'),
    '+225': ('225', 'Costa do Marfim'),
    '+221': ('221', 'Senegal'),
    '+237': ('237', 'Camarões'),
    '+250': ('250', 'Ruanda'),
}

@app.on_event("startup")
async def startup():
    init_db()

def detectar_pais(numero: str) -> Optional[str]:
    numero_limpo = numero.strip().replace(' ', '')
    for codigo_completo, (codigo, _) in PAIS_POR_CODIGO.items():
        if numero_limpo.startswith(codigo_completo) or numero_limpo.startswith(codigo):
            return codigo
    return None

@app.get("/")
async def root():
    return {
        "api": "Phone Validator API",
        "versao": "1.0.0",
        "paises_suportados": [
            "Moçambique", "Angola", "Brasil", "Portugal",
            "Cabo Verde", "Guiné-Bissau", "São Tomé e Príncipe", "Timor-Leste",
            "África do Sul", "Nigéria", "Quénia", "Tanzânia",
            "Gana", "Etiópia", "Zimbabué", "Zâmbia",
            "Egito", "Marrocos", "Argélia", "Uganda",
            "Costa do Marfim", "Senegal", "Camarões", "Ruanda",
            "Itália"
        ],
        "total_paises": 25,
        "docs": "/docs",
        "registar": "/registrar"
    }

@app.post("/registrar")
async def registrar(request: RegistroRequest):
    api_key = gerar_api_key(request.email)
    import sqlite3
    conn = sqlite3.connect('api_keys.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO api_keys (key_hash, plano, data_criacao) VALUES (?, ?, ?)',
        (api_key, request.plano, time.strftime('%Y-%m-%dT%H:%M:%S'))
    )
    conn.commit()
    conn.close()
    
    return {
        "sucesso": True,
        "api_key": api_key,
        "plano": request.plano,
        "mensagem": "Guarde esta chave. Use no header X-API-Key"
    }


@app.get("/demo")
async def demo_validar(numero: str = Query(...), request: Request = None):
    """Demonstração pública - sem API Key - limitado a 5 por hora por IP"""
    
    # Obter IP do visitante
    client_ip = request.client.host if request else "unknown"
    
    # Limpar registos antigos
    agora = datetime.now()
    demo_usage[client_ip] = [
        t for t in demo_usage[client_ip] 
        if agora - t < DEMO_WINDOW
    ]
    
    # Verificar limite
    if len(demo_usage[client_ip]) >= DEMO_LIMIT:
        raise HTTPException(
            status_code=429,
            detail=f"Limite de demonstração atingido ({DEMO_LIMIT} por hora). Registe-se para uso ilimitado: /registrar"
        )
    
    # Registar esta chamada
    demo_usage[client_ip].append(agora)
    
    # Validar
    phone_request = PhoneNumberRequest(numero=numero)
    return await validar_numero(phone_request)

@app.post("/validar", response_model=PhoneNumberResponse)
async def validar_numero(request: PhoneNumberRequest, api_key: str = Security(api_key_header)):
    if api_key:
        auth = verificar_api_key(api_key)
        if not auth:
            raise HTTPException(status_code=401, detail="API Key inválida")
    else:
        raise HTTPException(status_code=401, detail="API Key obrigatória. Registe-se em /registrar")
    
    numero = request.numero.strip()
    if not numero:
        raise HTTPException(status_code=400, detail="Número de telefone é obrigatório")
    
    codigo_pais = None
    if request.pais_hint:
        hints = {
            'MZ': '258', 'MOÇAMBIQUE': '258', 'MOZAMBIQUE': '258',
            'AO': '244', 'ANGOLA': '244',
            'BR': '55', 'BRASIL': '55','BRAZIL': '55',
            'PT': '351', 'PORTUGAL': '351',
            'IT': '39', 'ITALIA': '39', 'ITÁLIA': '39','ITALY': '39',
            'CV': '238', 'CABO VERDE': '238', 'CABO-VERDE': '238','CAPE-VERDE': '238',
            'GW': '245', 'GUINÉ-BISSAU': '245', 'GUINÉ': '245','GUINEA-BISSAU': '245',
            'ST': '239', 'SÃO TOMÉ': '239', 'SAO TOME': '239',
            'TL': '670', 'TIMOR-LESTE': '670', 'TIMOR': '670', 'EAST-TIMOR': '670',  'EAST TIMOR': '670',
            'ZA': '27', 'ÁFRICA DO SUL': '27', 'AFRICA DO SUL': '27', 'SOUTH AFRICA': '27',
            'NG': '234', 'NIGÉRIA': '234', 'NIGERIA': '234',
            'KE': '254', 'QUÉNIA': '254', 'QUENIA': '254', 'KENYA': '254',
            'TZ': '255', 'TANZÂNIA': '255', 'TANZANIA': '255',
            'GH': '233', 'GANA': '233', 'GHANA': '233',
            'ET': '251', 'ETIÓPIA': '251', 'ETIOPIA': '251', 'ETHIOPIA': '251',
            'ZW': '263', 'ZIMBABUÉ': '263', 'ZIMBABUE': '263', 'ZIMBABWE': '263',
            'ZM': '260', 'ZÂMBIA': '260', 'ZAMBIA': '260',
            'EG': '20', 'EGITO': '20', 'EGYPT': '20',
            'MA': '212', 'MARROCOS': '212', 'MOROCCO': '212',
            'DZ': '213', 'ARGÉLIA': '213', 'ALGERIA': '213',
            'UG': '256', 'UGANDA': '256',
            'CI': '225', 'COSTA DO MARFIM': '225', 'IVORY COAST': '225',
            'SN': '221', 'SENEGAL': '221',
            'CM': '237', 'CAMARÕES': '237', 'CAMEROON': '237',
            'RW': '250', 'RUANDA': '250', 'RWANDA': '250',
        }
        codigo_pais = hints.get(request.pais_hint.upper())
    
    if not codigo_pais:
        codigo_pais = detectar_pais(numero)
    
    if not codigo_pais:
        validator = InternacionalPhoneValidator(codigo_pais='+??', nome_pais='Desconhecido')
        resultado = validator.validar(numero)
        return PhoneNumberResponse(**resultado)
    
    validator = VALIDATORS.get(codigo_pais)
    if not validator:
        validator = InternacionalPhoneValidator(codigo_pais=f'+{codigo_pais}', nome_pais='Desconhecido')
    
    resultado = validator.validar(numero)
    return PhoneNumberResponse(**resultado)