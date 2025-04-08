class Pessoa:
    def __init__(self,nome,telefone,cpf,email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.email}'