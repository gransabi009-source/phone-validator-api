from datetime import datetime

PLANOS = {
    'gratis': {
        'nome': 'Grátis',
        'chamadas_mes': 100,
        'preco_mensal': 0,
        'preco_anual': 0,
        'recursos': ['Validação básica', '100 chamadas/mês', 'Suporte por email']
    },
    'basico': {
        'nome': 'Básico',
        'chamadas_mes': 5000,
        'preco_mensal': 9,
        'preco_anual': 90,
        'recursos': ['Validação completa', '5.000 chamadas/mês', 'Info de operadora', 'Suporte prioritário']
    },
    'profissional': {
        'nome': 'Profissional',
        'chamadas_mes': 25000,
        'preco_mensal': 29,
        'preco_anual': 290,
        'recursos': ['Tudo do Básico', '25.000 chamadas/mês', 'Bulk validation']
    },
    'empresarial': {
        'nome': 'Empresarial',
        'chamadas_mes': 100000,
        'preco_mensal': 99,
        'preco_anual': 990,
        'recursos': ['Tudo do Profissional', '100.000 chamadas/mês', 'SLA garantido']
    }
}

def get_plano_info(plano_nome: str):
    """Retorna info do plano ou None se não existir"""
    return PLANOS.get(plano_nome)