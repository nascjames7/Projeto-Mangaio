def impar(number):
    return (number % 2 == 1)

lista = []
quantidadeDeElementos = int(input('Digite a quantidade de elemnetos da lista: '))

for i in range(quantidadeDeElementos):
    numero = int(input('Digite um valor inteiro para completar a lista: '))
    lista.append(numero)
    
listaDeImpares = list(filter(impar, lista))
print('Os valores da lista numerica que sao impares: ', listaDeImpares) 

