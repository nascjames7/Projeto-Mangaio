try:
    number = int(input('Digite um número inteiro diferente de zero: '))
    if (number != 0): 
        number_square = number**2
        resultado01 = number_square + number   
        resultado02 = resultado01/number
        print(resultado02)            
    
except ZeroDivisionError:
    print('O número não pode ser igual a zero!')
