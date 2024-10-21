import sys
from pathlib import Path
file = Path(__file__).resolve()

parent, root = file.parent, file.parents[1]

sys.path.append(str(root))



from MODELS.pessoa import Pessoa
from typing import List
class PessoaController:
    pessoas = []
    
    @classmethod
    def salvar_pessoa(cls, pessoa:Pessoa) -> None:
        cls.pessoas.append(pessoa)
        
    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]:
        return cls.pessoas
    
    @classmethod
    def printPessoas(cls):
        for p in cls.pessoas:
            if(p != None):
                print("len:"+str(len(cls.pessoas)))
                print(p)
    
        
        
