try:
    number = float(input('Digite um número diferente de zero: '))
    number_square = number**2
    resultado = number_square/number
    print(resultado)#number    
    
except ZeroDivisionError:
    print('O número não pode ser igual a zero!')
except ValueError:
    print('Erro: Entrada inválida. Digite um número inteiro ou real.')
     

    
    
    