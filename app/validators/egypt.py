from .base import BasePhoneValidator
from typing import Dict, Tuple

class EgyptPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+20"
    
    @property
    def nome_pais(self) -> str:
        return "Egito"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '10': ('Vodafone', 'celular'),
            '11': ('Etisalat', 'celular'),
            '12': ('Orange', 'celular'),
            '15': ('WE', 'celular'),
            '2': ('Telecom Egypt', 'fixo'),
            '3': ('Telecom Egypt', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }