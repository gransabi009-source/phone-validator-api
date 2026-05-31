from .base import BasePhoneValidator
from typing import Dict, Tuple

class EthiopiaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+251"
    
    @property
    def nome_pais(self) -> str:
        return "Etiópia"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '91': ('Ethio Telecom', 'celular'),
            '92': ('Ethio Telecom', 'celular'),
            '93': ('Ethio Telecom', 'celular'),
            '94': ('Ethio Telecom', 'celular'),
            '95': ('Ethio Telecom', 'celular'),
            '96': ('Ethio Telecom', 'celular'),
            '97': ('Ethio Telecom', 'celular'),
            '98': ('Ethio Telecom', 'celular'),
            '99': ('Ethio Telecom', 'celular'),
            '11': ('Ethio Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }