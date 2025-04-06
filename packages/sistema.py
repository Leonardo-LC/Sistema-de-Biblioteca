from packages.pessoa import Pessoa


class Sistema:
    def __init__(self):
        self.acervo = {}
        self.clientes = {}

    def cadastrar_usuario(self,nome,telefone,cpf,email):
        self.clientes[nome] = Pessoa(nome,telefone,cpf,email)
        if nome in self.acervo:
            print(f'{nome} já está cadastrado!')
        else:
            print(f'{nome} foi cadastrado com sucesso!')

