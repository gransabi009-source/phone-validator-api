from .base import BasePhoneValidator
from typing import Dict, Tuple

class TanzaniaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+255"
    
    @property
    def nome_pais(self) -> str:
        return "Tanzânia"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '62': ('Halotel', 'celular'),
            '63': ('TTCL', 'celular'),
            '64': ('Airtel', 'celular'),
            '65': ('Tigo', 'celular'),
            '66': ('Airtel', 'celular'),
            '67': ('Tigo', 'celular'),
            '68': ('Airtel', 'celular'),
            '69': ('Airtel', 'celular'),
            '71': ('Tigo', 'celular'),
            '73': ('TTCL', 'celular'),
            '74': ('Vodacom', 'celular'),
            '75': ('Vodacom', 'celular'),
            '76': ('Vodacom', 'celular'),
            '77': ('Zantel', 'celular'),
            '78': ('Airtel', 'celular'),
            '79': ('Vodacom', 'celular'),
            '22': ('TTCL', 'fixo'),
            '26': ('Zantel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }