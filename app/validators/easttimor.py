from .base import BasePhoneValidator
from typing import Dict, Tuple

class EastTimorPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+670"
    
    @property
    def nome_pais(self) -> str:
        return "East-Timor"
    
    @property
    def tamanho_numero(self) -> int:
        return 11
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '77': ('Timor Telecom', 'celular'),
            '78': ('Timor Telecom', 'celular'),
            '75': ('Telkomcel', 'celular'),
            '76': ('Telkomcel', 'celular'),
            '73': ('Telemor', 'celular'),
            '74': ('Telemor', 'celular'),
            '21': ('Timor Telecom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }