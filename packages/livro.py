class Livro:
    def __init__(self,titulo,autor,ano,emprestado=False):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado = emprestado