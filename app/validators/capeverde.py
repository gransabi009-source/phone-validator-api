from .base import BasePhoneValidator
from typing import Dict, Tuple

class CapeVerdePhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+238"
    
    @property
    def nome_pais(self) -> str:
        return "Cape Verde"
    
    @property
    def tamanho_numero(self) -> int:
        return 10
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '91': ('CV Telecom', 'celular'),
            '92': ('CV Telecom', 'celular'),
            '93': ('CV Telecom', 'celular'),
            '95': ('Unitel T+', 'celular'),
            '97': ('Unitel T+', 'celular'),
            '98': ('Unitel T+', 'celular'),
            '99': ('CV Telecom', 'celular'),
            '2': ('CV Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }