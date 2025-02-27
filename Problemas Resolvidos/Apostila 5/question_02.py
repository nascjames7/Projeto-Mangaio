class Livro:
 def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor
 
 def apresentar(self):
     print(f'O título do livro é {self.titulo} e o autor(a) é {self.autor}.')
 
titulo_do_livro = input('Digite o título do livro: ')
nome_do_autor = input('Digite o nome do autor(a): ')
livro01 = Livro(titulo_do_livro, nome_do_autor)
livro01.apresentar()