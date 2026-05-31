from .base import BasePhoneValidator
from typing import Dict, Tuple

class GhanaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+233"
    
    @property
    def nome_pais(self) -> str:
        return "Gana"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '20': ('Vodafone', 'celular'),
            '23': ('Globacom', 'celular'),
            '24': ('MTN', 'celular'),
            '25': ('MTN', 'celular'),
            '26': ('AirtelTigo', 'celular'),
            '27': ('AirtelTigo', 'celular'),
            '50': ('Vodafone', 'celular'),
            '53': ('Globacom', 'celular'),
            '54': ('MTN', 'celular'),
            '55': ('MTN', 'celular'),
            '56': ('AirtelTigo', 'celular'),
            '57': ('AirtelTigo', 'celular'),
            '59': ('MTN', 'celular'),
            '30': ('Vodafone', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }