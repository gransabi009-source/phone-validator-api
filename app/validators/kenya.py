from .base import BasePhoneValidator
from typing import Dict, Tuple

class KenyaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+254"
    
    @property
    def nome_pais(self) -> str:
        return "Quénia"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '10': ('Airtel', 'celular'),
            '11': ('Safaricom', 'celular'),
            '12': ('Telkom Kenya', 'celular'),
            '70': ('Safaricom', 'celular'),
            '71': ('Safaricom', 'celular'),
            '72': ('Safaricom', 'celular'),
            '73': ('Airtel', 'celular'),
            '74': ('Safaricom', 'celular'),
            '75': ('Airtel', 'celular'),
            '76': ('Safaricom', 'celular'),
            '77': ('Telkom Kenya', 'celular'),
            '78': ('Airtel', 'celular'),
            '79': ('Safaricom', 'celular'),
            '20': ('Telkom Kenya', 'fixo'),
            '41': ('Telkom Kenya', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }