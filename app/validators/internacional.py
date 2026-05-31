from .base import BasePhoneValidator
from typing import Dict, Tuple
import re

class InternacionalPhoneValidator(BasePhoneValidator):
    
    def __init__(self, codigo_pais: str, nome_pais: str, tamanho_numero: int = None):
        self._codigo_pais = codigo_pais
        self._nome_pais = nome_pais
        self._tamanho_numero = tamanho_numero
    
    @property
    def codigo_pais(self) -> str:
        return self._codigo_pais
    
    @property
    def nome_pais(self) -> str:
        return self._nome_pais
    
    @property
    def tamanho_numero(self) -> int:
        return self._tamanho_numero or 10
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {}
    
    def validar(self, numero: str) -> Dict:
        numero_original = numero
        numero_limpo = self.limpar_numero(numero)
        
        if not numero_limpo.startswith('+'):
            if numero_limpo.startswith(self._codigo_pais.replace('+', '')):
                numero_limpo = f"+{numero_limpo}"
            else:
                numero_limpo = f"{self._codigo_pais}{numero_limpo}"
        
        apenas_digitos = numero_limpo.replace('+', '')
        formato_valido = bool(re.match(r'^\+?[1-9]\d{6,14}$', numero_limpo))
        
        valido = formato_valido
        
        return {
            'numero_original': numero_original,
            'numero_normalizado': numero_limpo if valido else None,
            'pais': self._nome_pais,
            'codigo_pais': self._codigo_pais,
            'operadora': None,
            'tipo': None,
            'valido': valido,
            'informacao_extra': {
                'prefixo': '',
                'tamanho_correto': str(True),
                'formato_internacional': ''
            }
        }