import sys
sys.path.append(".")
from src.MODELS import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa("Luiz", "Gadelha", 33, 111100)
    assert p1.nome_completo() == 'Luiz Gadelha'
    
    