from .base import BasePhoneValidator
from typing import Dict, Tuple

class AlgeriaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+213"
    
    @property
    def nome_pais(self) -> str:
        return "Argélia"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '5': ('Djezzy', 'celular'),
            '6': ('Mobilis', 'celular'),
            '7': ('Ooredoo', 'celular'),
            '21': ('Algérie Télécom', 'fixo'),
            '41': ('Algérie Télécom', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }