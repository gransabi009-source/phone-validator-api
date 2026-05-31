from .base import BasePhoneValidator
from typing import Dict, Tuple

class PortugalPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+351"
    
    @property
    def nome_pais(self) -> str:
        return "Portugal"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '91': ('Vodafone', 'celular'),
            '92': ('Vodafone', 'celular'),
            '93': ('NOS', 'celular'),
            '96': ('MEO', 'celular'),
            '21': ('MEO', 'fixo'),
            '22': ('NOS', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }