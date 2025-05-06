import random

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = str(random.randint(1000, 9999))  # ID com 4 dígitos

class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, preco_diaria):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.disponivel = True

class Reserva:
    def __init__(self, dono, quarto, data_in, data_out, status):
        self.dono = dono
        self.quarto = quarto
        self.data_in = data_in
        self.data_out = data_out
        self.status = status

class GerenciamentoDeReserva:
    def __init__(self):        
        self.clientes = []  
        self.quartos = []
        self.reservas = []

    def verificar_quarto(self, num_quarto):
        for quarto in self.quartos:
            if quarto.numero_quarto == num_quarto:
                return quarto.disponivel
        print("Quarto não encontrado.")
        return False  

    def adicionar_quarto(self, numero_quarto, tipo_quarto, preco_diaria):
        novo_quarto = Quarto(numero_quarto, tipo_quarto, preco_diaria)
        self.quartos.append(novo_quarto)
        print(f"Quarto {numero_quarto} adicionado com sucesso!")

    def adicionar_cliente(self, nome, telefone, email):
        novo_cliente = Cliente(nome, telefone, email)
        
        # Evitar IDs duplicados
        while any(cliente.id_unico == novo_cliente.id_unico for cliente in self.clientes):
            novo_cliente.id_unico = str(random.randint(1000, 9999))
        
        self.clientes.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso! ID: {novo_cliente.id_unico}")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        print("\nLista de Clientes:")
        for cliente in self.clientes:
            print(f"ID: {cliente.id_unico} | Nome: {cliente.nome} | Telefone: {cliente.telefone} | E-mail: {cliente.email}")

    def deletar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_unico == id_cliente:
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nome} removido com sucesso.")
                return
        print("Cliente não encontrado.")

# Criando o sistema de gerenciamento
refugio_dos_sonhos = GerenciamentoDeReserva()

while True:
    print("\n1 = Adicionar Quarto")
    print("2 = Verificar Disponibilidade do Quarto")
    print("3 = Adicionar Cliente")
    print("4 = Listar Clientes")
    print("5 = Deletar Cliente")
    print("6 = Sair")
    
    try:
        op = int(input("-> "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if op == 1:
        try:
            num = int(input("Digite o Número do Quarto: "))
            tipo = input("Digite o Tipo do Quarto:  [Simples, Duplo, Triplo]: ")
            valor = float(input("Digite o valor da Diária: "))
            refugio_dos_sonhos.adicionar_quarto(num, tipo, valor)
        except ValueError:
            print("Erro: Número do quarto deve ser um inteiro e o valor da diária deve ser um número.")

    elif op == 2:
        try:
            num = int(input("Digite o Número do Quarto para verificar: "))
            disponivel = refugio_dos_sonhos.verificar_quarto(num)
            if disponivel:
                print(f"\nO quarto {num} está disponível.")
            else:
                print(f"\nO quarto {num} não está disponível ou não existe.")
        except ValueError:
            print("\nErro: Digite um número válido.")

    elif op == 3:
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        refugio_dos_sonhos.adicionar_cliente(nome, telefone, email)

    elif op == 4:
        refugio_dos_sonhos.listar_clientes()

    elif op == 5:
        refugio_dos_sonhos.listar_clientes()  # Mostra os clientes antes de deletar
        id_cliente = input("Digite o ID do cliente que deseja remover: ")
        refugio_dos_sonhos.deletar_cliente(id_cliente)

    elif op == 6:
        print("Encerrando o programa...\n\n")
        break

    else:
        print("Opção inválida, tente novamente.")
