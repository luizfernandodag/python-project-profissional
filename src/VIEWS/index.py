import sys
from pathlib import Path
#print(__file__)
file = Path(__file__).resolve()

parent, root = file.parent, file.parents[1]

sys.path.append(str(root))

from CONTROLLERS.pessoaControler import PessoaController
from MODELS.pessoa import Pessoa


import sys
print(sys.executable)

while (True):
    decisao = int(input("Digite 1 para salvar, 2 para listar e para 3 sair"))
    
    if(decisao ==1 ):
        nome = input('Nome:')
        sobrenome = input('Sobrenome:')
        idade = int(input('Idade:'))
        cpf = input('cpf:')
        
        p1= Pessoa(nome, sobrenome, idade, cpf)
        PessoaController.salvar_pessoa(p1)
    elif(decisao == 2):
        PessoaController.printPessoas()
    elif(decisao == 3):
        break