from .base import BasePhoneValidator
from typing import Dict, Tuple

class MoroccoPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+212"
    
    @property
    def nome_pais(self) -> str:
        return "Marrocos"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '6': ('Maroc Telecom', 'celular'),
            '7': ('Maroc Telecom', 'celular'),
            '61': ('Orange', 'celular'),
            '62': ('Orange', 'celular'),
            '66': ('Inwi', 'celular'),
            '67': ('Inwi', 'celular'),
            '5': ('Maroc Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }