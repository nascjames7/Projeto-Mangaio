from functools import reduce

def adicao(valor01, valor02):
    return valor01 +valor02

lista = []
quantidadeDeElementos = int(input('Digite a quantidade de elemnetos da lista: '))

for i in range(quantidadeDeElementos):
    numero = int(input('Digite um valor inteiro para completar a lista: '))
    lista.append(numero)
    
somaTotal = reduce(adicao, lista)
print('O somatorio dos valores da lista: ', somaTotal)