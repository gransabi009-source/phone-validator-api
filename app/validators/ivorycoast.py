from .base import BasePhoneValidator
from typing import Dict, Tuple

class IvoryCoastPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+225"
    
    @property
    def nome_pais(self) -> str:
        return "Costa do Marfim"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '01': ('Orange', 'celular'),
            '05': ('MTN', 'celular'),
            '07': ('Moov', 'celular'),
            '21': ('Orange', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }