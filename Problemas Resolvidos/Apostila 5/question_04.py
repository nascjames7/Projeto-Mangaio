class Funcionario:
 def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario
 
 def apresentar(self):
     print(f'O nome do funcionário(a) é {self.nome} e o salario inicial é {self.salario} reais.')
 
nome_do_funcionario = input('Digite o nome do(a) funcionário(a): ')
salario_do_funcionario = float(input('Digite o salário do(a) funcionário(a): '))
porcentagem = float(input('Digite a porcentagem do aumento de salário: '))

class Gerente(Funcionario):
    
    def aumentar_salario(self):
        novo_salario = (salario_do_funcionario * (1 + porcentagem/100))        
        print(f'O novo salário de {nome_do_funcionario} é {novo_salario} reais.')

funcionario01 = Gerente(nome_do_funcionario, salario_do_funcionario)
funcionario01.apresentar()
funcionario01.aumentar_salario()