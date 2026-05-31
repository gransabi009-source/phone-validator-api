from .base import BasePhoneValidator
from typing import Dict, Tuple

class GuineaBissauPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+245"
    
    @property
    def nome_pais(self) -> str:
        return "Guinea-Bissau"
    
    @property
    def tamanho_numero(self) -> int:
        return 10
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '95': ('Orange', 'celular'),
            '96': ('Orange', 'celular'),
            '97': ('Orange', 'celular'),
            '90': ('MTN', 'celular'),
            '91': ('MTN', 'celular'),
            '92': ('MTN', 'celular'),
            '93': ('MTN', 'celular'),
            '94': ('MTN', 'celular'),
            '44': ('Guiné Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }