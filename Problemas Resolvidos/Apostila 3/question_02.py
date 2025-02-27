def fatorial(numeroInteiro):
    if(numeroInteiro == 0):return 1
    else:return (numeroInteiro * fatorial(numeroInteiro - 1))     
  
souNumeroInteiro = int(input('Digite um numero inteiro: '))
print(f'O fatorial do numero {souNumeroInteiro} eh: ', fatorial(souNumeroInteiro))

