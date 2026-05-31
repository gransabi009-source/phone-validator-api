from .base import BasePhoneValidator
from typing import Dict, Tuple

class BrazilPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+55"
    
    @property
    def nome_pais(self) -> str:
        return "Brazil"
    
    @property
    def tamanho_numero(self) -> int:
        return 13
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '11': ('São Paulo', 'celular/fixo'),
            '21': ('Rio de Janeiro', 'celular/fixo'),
            '31': ('Minas Gerais', 'celular/fixo'),
            '41': ('Paraná', 'celular/fixo'),
            '51': ('Rio Grande do Sul', 'celular/fixo'),
            '61': ('Distrito Federal', 'celular/fixo'),
            '71': ('Bahia', 'celular/fixo'),
            '81': ('Pernambuco', 'celular/fixo'),
            '91': ('Pará', 'celular/fixo'),
            '92': ('Amazonas', 'celular/fixo'),
        }