def potencia(number):
    return (number ** 2)

lista = []
quantidadeDeElementos = int(input('Digite a quantidade de elemnetos da lista: '))

for i in range(quantidadeDeElementos):
    numero = int(input('Digite um valor inteiro para completar a lista: '))
    lista.append(numero)
    
listaDeQuadrados = list(map(potencia, lista))
print('Os valores da lista numerica elevada ao quadrado: ', listaDeQuadrados) 