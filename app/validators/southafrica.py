from .base import BasePhoneValidator
from typing import Dict, Tuple

class SouthAfricaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+27"
    
    @property
    def nome_pais(self) -> str:
        return "África do Sul"
    
    @property
    def tamanho_numero(self) -> int:
        return 11
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '10': ('Telkom', 'fixo'),
            '11': ('Telkom', 'fixo'),
            '12': ('Telkom', 'fixo'),
            '13': ('Telkom', 'fixo'),
            '14': ('Telkom', 'fixo'),
            '15': ('Telkom', 'fixo'),
            '16': ('Telkom', 'fixo'),
            '17': ('Telkom', 'fixo'),
            '18': ('Telkom', 'fixo'),
            '21': ('Telkom', 'fixo'),
            '31': ('Telkom', 'fixo'),
            '41': ('Telkom', 'fixo'),
            '51': ('Telkom', 'fixo'),
            '60': ('MTN', 'celular'),
            '61': ('Cell C', 'celular'),
            '62': ('Cell C', 'celular'),
            '63': ('MTN', 'celular'),
            '64': ('Cell C', 'celular'),
            '65': ('Cell C', 'celular'),
            '66': ('Vodacom', 'celular'),
            '67': ('Vodacom', 'celular'),
            '68': ('Vodacom', 'celular'),
            '69': ('Vodacom', 'celular'),
            '70': ('MTN', 'celular'),
            '71': ('Vodacom', 'celular'),
            '72': ('Vodacom', 'celular'),
            '73': ('MTN', 'celular'),
            '74': ('Cell C', 'celular'),
            '76': ('Vodacom', 'celular'),
            '78': ('MTN', 'celular'),
            '79': ('Vodacom', 'celular'),
            '80': ('Telkom Mobile', 'celular'),
            '81': ('Telkom Mobile', 'celular'),
            '82': ('Vodacom', 'celular'),
            '83': ('MTN', 'celular'),
            '84': ('Cell C', 'celular'),
            '800': ('Gratuito', 'gratuito'),
        }