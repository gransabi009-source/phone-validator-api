from .base import BasePhoneValidator
from typing import Dict, Tuple

class ZimbabwePhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+263"
    
    @property
    def nome_pais(self) -> str:
        return "Zimbabwe"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '71': ('NetOne', 'celular'),
            '73': ('Telecel', 'celular'),
            '77': ('Econet', 'celular'),
            '78': ('Econet', 'celular'),
            '4': ('TelOne', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }