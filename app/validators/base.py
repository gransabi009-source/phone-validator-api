from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple
import re

class BasePhoneValidator(ABC):
    @property
    @abstractmethod
    def codigo_pais(self) -> str:
        pass
    
    @property
    @abstractmethod
    def nome_pais(self) -> str:
        pass
    
    @property
    @abstractmethod
    def tamanho_numero(self) -> int:
        pass
    
    @abstractmethod
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        pass
    
    def limpar_numero(self, numero: str) -> str:
        return re.sub(r'[\s\-\(\)\.]', '', numero)
    
    def extrair_prefixo(self, numero_limpo: str) -> Optional[str]:
        codigo_sem_mais = self.codigo_pais.replace('+', '')
        
        if numero_limpo.startswith(codigo_sem_mais):
            numero_local = numero_limpo[len(codigo_sem_mais):]
        elif numero_limpo.startswith('0'):
            numero_local = numero_limpo[1:]
        else:
            numero_local = numero_limpo
        
        for tamanho in [3, 2]:
            prefixo = numero_local[:tamanho]
            if prefixo in self.get_operadoras():
                return prefixo
        
        return None
    
    def validar(self, numero: str) -> Dict:
        numero_original = numero
        numero_limpo = self.limpar_numero(numero)
        codigo_sem_mais = self.codigo_pais.replace('+', '')
        
        if numero_limpo.startswith('+'):
            numero_limpo_com_codigo = numero_limpo
        elif numero_limpo.startswith(codigo_sem_mais):
            numero_limpo_com_codigo = f"+{numero_limpo}"
        elif numero_limpo.startswith('0'):
            numero_limpo_com_codigo = f"{self.codigo_pais}{numero_limpo[1:]}"
        else:
            numero_limpo_com_codigo = f"{self.codigo_pais}{numero_limpo}"
        
        apenas_digitos = numero_limpo_com_codigo.replace('+', '')
        tamanho_correto = len(apenas_digitos) == self.tamanho_numero
        prefixo = self.extrair_prefixo(apenas_digitos)
        operadoras = self.get_operadoras()
        
        valido = tamanho_correto and prefixo is not None
        operadora_info = operadoras.get(prefixo, (None, None)) if prefixo else (None, None)
        
        return {
            'numero_original': numero_original,
            'numero_normalizado': numero_limpo_com_codigo if valido else None,
            'pais': self.nome_pais,
            'codigo_pais': self.codigo_pais,
            'operadora': operadora_info[0],
            'tipo': operadora_info[1],
            'valido': valido,
            'informacao_extra': {
                'prefixo': prefixo or '',
                'tamanho_correto': str(tamanho_correto),
                'formato_internacional': f"{self.codigo_pais} {prefixo} {apenas_digitos[-7:]}" if valido and prefixo else ''
            }
        }