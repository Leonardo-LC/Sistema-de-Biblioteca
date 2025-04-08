from pessoa import Pessoa

class Sistema:
    def __init__(self):
        self.acervo = {}
        self.clientes = {}

    def cadastrar_usuario(self,nome,telefone,cpf,email):
        if nome in self.clientes:
            print(f'{nome} já está cadastrado!')
        else:
            self.clientes[nome] = Pessoa(nome,telefone,cpf,email)
            print(f'{nome} foi cadastrado com sucesso!')

    def editar_usuario(self,nome,novo_telefone,novo_email):
       if nome not in self.clientes:
           print(f'{nome} não está cadastrado!')
       else:
           self.clientes[nome].telefone = novo_telefone
           self.clientes[nome].email = novo_email
           print(f'{nome} foi editado com sucesso!')

