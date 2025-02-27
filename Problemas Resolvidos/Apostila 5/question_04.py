class Veiculo:
    def tipo(self):
        pass

class Carro(Veiculo):
    def tipo(self):
        return "carro"

class Moto(Veiculo):
    def tipo(self):
        return "moto"

veiculo01 = Carro()
veiculo02 = Moto()

print(veiculo01.tipo())  
print(veiculo02.tipo())  