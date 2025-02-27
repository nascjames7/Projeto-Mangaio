class Aluno:
 def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota
 
 def apresentar(self):
     if(self.nota >= 7):print(f'Olá, meu nome é {self.nome} e a minha nota é {self.nota}. Situação do aluno(a): APROVADO!')
     else:print(f'Olá, meu nome é {self.nome} e a minha nota é {self.nota} anos. Situação do aluno(a): REPROVADO!')
 
nome_do_aluno = input('Digite o nome do aluno(a): ')
nota_do_aluno = float(input('Digite a nota do aluno(a): '))
aluno01 = Aluno(nome_do_aluno, nota_do_aluno)
aluno01.apresentar()