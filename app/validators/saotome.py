from .base import BasePhoneValidator
from typing import Dict, Tuple

class SaoTomePhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+239"
    
    @property
    def nome_pais(self) -> str:
        return "São Tomé e Príncipe"
    
    @property
    def tamanho_numero(self) -> int:
        return 10
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '90': ('CST', 'celular'),
            '98': ('CST', 'celular'),
            '99': ('CST', 'celular'),
            '22': ('CST', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }