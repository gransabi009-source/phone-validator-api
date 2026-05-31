from .base import BasePhoneValidator
from typing import Dict, Tuple

class MozambiquePhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+258"
    
    @property
    def nome_pais(self) -> str:
        return "Mozambique"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '84': ('Vodacom', 'celular'),
            '85': ('Vodacom', 'celular'),
            '82': ('Tmcel', 'celular'),
            '83': ('Tmcel', 'celular'),
            '86': ('Movitel', 'celular'),
            '87': ('Movitel', 'celular'),
            '21': ('Tmcel', 'fixo'),
            '22': ('Tmcel', 'fixo'),
            '23': ('Tmcel', 'fixo'),
            '24': ('Tmcel', 'fixo'),
            '25': ('Tmcel', 'fixo'),
            '26': ('Tmcel', 'fixo'),
            '27': ('Tmcel', 'fixo'),
            '28': ('Tmcel', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
            '30': ('Premium', 'premium'),
        }