class Pessoa:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def __repr__(self) -> str:
        return f"Pessoa [ Nome: {self.nome}, Sobrenome: {self.sobrenome} Idade: {self.idade} cpf: {self.cpf}]"
        
        
        
        
        
        