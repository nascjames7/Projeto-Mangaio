def maiorNumero(firstNumber, secondNumber):
    if(firstNumber >= secondNumber):maior = firstNumber
    else:maior = secondNumber
    return maior
    
first = float(input('Digite o primeiro valor: '))
second = float(input('Digite o segundo valor: '))
print('O maior valor numerico eh: ', maiorNumero(first, second))