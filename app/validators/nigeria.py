from .base import BasePhoneValidator
from typing import Dict, Tuple

class NigeriaPhoneValidator(BasePhoneValidator):
    
    @property
    def codigo_pais(self) -> str:
        return "+234"
    
    @property
    def nome_pais(self) -> str:
        return "Nigéria"
    
    @property
    def tamanho_numero(self) -> int:
        return 13
    
    def get_operadoras(self) -> Dict[str, Tuple[str, str]]:
        return {
            '701': ('Airtel', 'celular'),
            '702': ('Airtel', 'celular'),
            '703': ('MTN', 'celular'),
            '704': ('MTN', 'celular'),
            '705': ('Glo', 'celular'),
            '706': ('MTN', 'celular'),
            '707': ('MTN', 'celular'),
            '708': ('Airtel', 'celular'),
            '709': ('9mobile', 'celular'),
            '802': ('Airtel', 'celular'),
            '803': ('MTN', 'celular'),
            '804': ('MTN', 'celular'),
            '805': ('Glo', 'celular'),
            '806': ('MTN', 'celular'),
            '807': ('Glo', 'celular'),
            '808': ('Airtel', 'celular'),
            '809': ('9mobile', 'celular'),
            '810': ('MTN', 'celular'),
            '811': ('Glo', 'celular'),
            '812': ('Airtel', 'celular'),
            '813': ('MTN', 'celular'),
            '814': ('MTN', 'celular'),
            '815': ('Glo', 'celular'),
            '816': ('MTN', 'celular'),
            '817': ('9mobile', 'celular'),
            '818': ('9mobile', 'celular'),
            '901': ('Airtel', 'celular'),
            '902': ('Airtel', 'celular'),
            '903': ('MTN', 'celular'),
            '904': ('Airtel', 'celular'),
            '905': ('Glo', 'celular'),
            '906': ('MTN', 'celular'),
            '907': ('9mobile', 'celular'),
            '908': ('9mobile', 'celular'),
            '909': ('9mobile', 'celular'),
            '1': ('NITEL', 'fixo'),
            '2': ('NITEL', 'fixo'),
            '800': ('Gratuito', 'gratuito'),
        }