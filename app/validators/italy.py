from .base import BasePhoneValidator
from typing import Dict, Tuple

class ItalyPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+39"
    
    @property
    def nome_pais(self) -> str:
        return "Italy"
    
    @property
    def tamanho_numero(self) -> int:
        return 12
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '330': ('TIM', 'celular'),
            '331': ('TIM', 'celular'),
            '333': ('TIM', 'celular'),
            '334': ('TIM', 'celular'),
            '335': ('Vodafone', 'celular'),
            '336': ('TIM', 'celular'),
            '337': ('Vodafone', 'celular'),
            '338': ('TIM', 'celular'),
            '339': ('Vodafone', 'celular'),
            '340': ('Vodafone', 'celular'),
            '345': ('Vodafone', 'celular'),
            '346': ('Vodafone', 'celular'),
            '347': ('Vodafone', 'celular'),
            '348': ('Vodafone', 'celular'),
            '349': ('Vodafone', 'celular'),
            '320': ('Wind Tre', 'celular'),
            '324': ('Wind Tre', 'celular'),
            '327': ('Wind Tre', 'celular'),
            '328': ('Wind Tre', 'celular'),
            '329': ('Wind Tre', 'celular'),
            '350': ('Iliad', 'celular'),
            '351': ('Iliad', 'celular'),
            '02': ('Milão', 'fixo'),
            '06': ('Roma', 'fixo'),
            '010': ('Génova', 'fixo'),
            '011': ('Turim', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }