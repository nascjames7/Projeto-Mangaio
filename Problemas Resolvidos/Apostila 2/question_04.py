lista_numeros = []
contador = 0
for i in range(3):
    numero = float(input('Digite o {}º valor para a lista: '.format(i)))
    lista_numeros.append(numero)   
valor = float(input('Digite um valor qualquer: '))
for i in range(3):
    if valor == lista_numeros[i]: 
        print('O valor {} faz parte da lista!'.format(valor))
        contador += 1
        break
if contador == 0: print('Nenhum numero da lista eh equivalente ao valor procurado!')
        
    
    
