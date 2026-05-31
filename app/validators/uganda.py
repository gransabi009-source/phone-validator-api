from .base import BasePhoneValidator
from typing import Dict, Tuple

class UgandaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+256"
    
    @property
    def nome_pais(self) -> str:
        return "Uganda"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '70': ('Airtel', 'celular'),
            '71': ('MTN', 'celular'),
            '72': ('Airtel', 'celular'),
            '73': ('Airtel', 'celular'),
            '74': ('Airtel', 'celular'),
            '75': ('MTN', 'celular'),
            '76': ('MTN', 'celular'),
            '77': ('MTN', 'celular'),
            '78': ('MTN', 'celular'),
            '79': ('Airtel', 'celular'),
            '20': ('Uganda Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }