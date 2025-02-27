class Veiculo:
 def __init__(self, modelo, cor):    
    self.modelo = modelo
    self.cor = cor
 
 def apresentar(self):
     print(f'modelo {self.modelo} e cor{self.cor}') 

class Carro(Veiculo):
    def mostrar_tipo(self):
        print('tipo: carro')        
            
class Moto(Veiculo):
    def mostrar_tipo(self):
        print('tipo: moto')
      
modelo_do_veiculo01 = input('Digite o modelo do veiculo01: ')
modelo_do_veiculo02 = input('Digite o modelo do veiculo02: ')
cor_do_veiculo01 = input('Digite a cor do veiculo 01: ')
cor_do_veiculo02 = input('Digite a cor do veiculo 02: ')
    
veiculo01 = Carro(modelo_do_veiculo01, cor_do_veiculo01)
veiculo02 = Moto(modelo_do_veiculo02, cor_do_veiculo02)
veiculo01.apresentar()
veiculo01.mostrar_tipo()
veiculo02.apresentar()
veiculo02.mostrar_tipo()
