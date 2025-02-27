def tipoDeNumero(number):
    if(number%2 == 0):mensagem = 'O número é par!'
    else:mensagem = 'O número é ímpar!'
    return mensagem  
    
numero = int(input('Digite o número: '))
print(tipoDeNumero(numero))