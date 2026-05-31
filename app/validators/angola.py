from .base import BasePhoneValidator
from typing import Dict, Tuple

class AngolaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+244"
    
    @property
    def nome_pais(self) -> str:
        return "Angola"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '923': ('Unitel', 'celular'),
            '925': ('Unitel', 'celular'),
            '93': ('Unitel', 'celular'),
            '94': ('Unitel', 'celular'),
            '91': ('Movicel', 'celular'),
            '99': ('Movicel', 'celular'),
            '222': ('Angola Telecom', 'fixo'),
            '232': ('Angola Telecom', 'fixo'),
        }