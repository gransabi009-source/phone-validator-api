from .base import BasePhoneValidator
from typing import Dict, Tuple

class CameroonPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+237"
    
    @property
    def nome_pais(self) -> str:
        return "Camarões"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '6': ('MTN', 'celular'),
            '67': ('MTN', 'celular'),
            '68': ('MTN', 'celular'),
            '69': ('Orange', 'celular'),
            '65': ('Orange', 'celular'),
            '66': ('Orange', 'celular'),
            '2': ('Camtel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }