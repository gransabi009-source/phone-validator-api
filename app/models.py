from pydantic import BaseModel
from typing import Optional, Dict

class PhoneNumberRequest(BaseModel):
    numero: str
    pais_hint: Optional[str] = None

class PhoneNumberResponse(BaseModel):
    numero_original: str
    numero_normalizado: Optional[str] = None
    pais: Optional[str] = None
    codigo_pais: Optional[str] = None
    operadora: Optional[str] = None
    tipo: Optional[str] = None
    valido:bool
    informacao_extra: Dict[str, str]
    erro: Optional[str] = None

class RegistroRequest(BaseModel):
    email: str
    nome: str
    plano: str = "gratis"