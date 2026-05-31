from .base import BasePhoneValidator
from typing import Dict, Tuple

class ZambiaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+260"
    
    @property
    def nome_pais(self) -> str:
        return "Zâmbia"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '95': ('Zamtel', 'celular'),
            '96': ('MTN', 'celular'),
            '97': ('Airtel', 'celular'),
            '76': ('MTN', 'celular'),
            '77': ('Airtel', 'celular'),
            '21': ('Zamtel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }