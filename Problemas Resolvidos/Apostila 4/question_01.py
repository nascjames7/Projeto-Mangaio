try:
    number = float(input('Digite um número inteiro diferente de zero: '))
    resultado = number/number
    
except ZeroDivisionError:
    print('O número não pode ser igual a zero!')
except ValueError:
    print('Erro: Entrada inválida. Digite um número inteiro.')
     
    
    