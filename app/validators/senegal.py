from .base import BasePhoneValidator
from typing import Dict, Tuple

class SenegalPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+221"
    
    @property
    def nome_pais(self) -> str:
        return "Senegal"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '70': ('Orange', 'celular'),
            '76': ('Free', 'celular'),
            '77': ('Orange', 'celular'),
            '78': ('Orange', 'celular'),
            '33': ('Sonatel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }