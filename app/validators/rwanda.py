from .base import BasePhoneValidator
from typing import Dict, Tuple

class RwandaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+250"
    
    @property
    def nome_pais(self) -> str:
        return "Ruanda"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '72': ('Airtel', 'celular'),
            '73': ('Airtel', 'celular'),
            '78': ('MTN', 'celular'),
            '79': ('MTN', 'celular'),
            '25': ('Airtel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }