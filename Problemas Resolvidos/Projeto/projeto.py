import hashlib

users = []

def hash_senha(senha_do_usuario):
    return hashlib.sha256(senha_do_usuario.encode()).hexdigest()

def cadastrar_usuario():
    nome_do_usuario = input('Digite o nome de um(a) usuário(a): ')    
    for user in users:
        if user['nome'] == nome_do_usuario:
            print("Usuário(a) já existe. Tente novamente.")
            return

    senha_do_usuario = input("Digite a senha: ")   
    senha_hash = hash_senha(senha_do_usuario)
    
    users.append({'nome': nome_do_usuario, 'senha': senha_hash})
    print(f"Usuário {nome_do_usuario} cadastrado.")

def login_usuario():
    nome_do_usuario = input("Digite o nome do(a) usuário(a): ")
    senha_do_usuario = input("Digite a senha: ")
    senha_hash = hash_senha(senha_do_usuario)
    
    for user in users:
        if user['nome'] == nome_do_usuario and user['senha'] == senha_hash:
            print("Login bem-sucedido!")
            return user  
    
    print("Nome ou senha incorretos. Talvez estes dados não eestejam cadastrados no sistema!")
    return None

def aprovar_senha(senha):
    if len(senha) < 8:
        print('A senha precisa ser constituída por pelo menos 8 caracteres.')
        return False
    elif not any(char.isdigit() for char in senha):
        print('A senha deve consistir de no mínimo um número.')
        return False
    elif not any(char.isalpha() for char in senha):
        print('A senha deve consistir de no mínimo uma letra.')
        return False
    return True

def update_senha(user):
    senha_atual = input('Digite a senha atual: ')
    senha_atual_hash = hash_senha(senha_atual)
    
    if user['senha'] != senha_atual_hash:
        print('Senha atual incorreta.')
    return  
        

    nova_senha = input("Digite uma nova senha: ")    
    
    if not update_senha(nova_senha):
        return

    nova_senha_hash = hash_senha(nova_senha)
    user['senha'] = nova_senha_hash
    print("Senha alterada com sucesso.")


def menu_principal():
    while True:
        print("\n1. Adicionar usuário")
        print("2. Realizar login")
        print("3. Atualizar senha")
        print("4. Sair")
        opcao = input("Digite uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            usuario_logado = login_usuario()
            if usuario_logado:
                while True:
                    print("\n1. Alterar senha")
                    print("2. Sair")
                    opcao_logado = input("Escolha uma opção: ")

                    if opcao_logado == '1':
                        update_senha(usuario_logado)
                    elif opcao_logado == '2':
                        break
        elif opcao == '3':
            print("É necesssário estar conectado para alterar a senha.")
        elif opcao == '4':
            print("Você saiu do sistema!")
            break
        else:
            print("A opção não é válida.")

# Executa o menu principal
if __name__ == "__main__":
    menu_principal()
    