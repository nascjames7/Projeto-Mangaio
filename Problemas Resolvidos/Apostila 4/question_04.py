
class MeuErro(Exception):
    pass
try:
    name = input('Digite quaisquer tipo de Strings: ')
    print(name)
    if(name.isdigit()):        
        raise MeuErro("Ocorreu um erro personalizado!")   
    
except MeuErro as e:
    print('Um número foi digitado no lugar de uma String!')    
    print('Erro capturado: ', e)