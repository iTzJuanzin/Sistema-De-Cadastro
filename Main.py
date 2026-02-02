usuarios = []

def CadastrarUsuario(usuarios):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    usuario = {
            "nome": nome, 
            "idade": idade
        }

    usuarios.append(usuario)
        
    print("usario cadastrado com sucesso!")

def BuscarUsuario(usuarios):
    busca = input("Digite o nome do usuário que deseja buscar: ").lower()
    encontrado = False

    for user in usuarios:
            if user['nome'].lower() == busca:
                print(f"Usuário encontrado: Nome: {user['nome']}, Idade: {user['idade']}")
                encontrado = True
                
    if not encontrado:
            print("Usuário não encontrado.")

def ListarUsuarios(usuarios):
    if not usuarios:
            print("Nenhum usuário cadastrado.")
    else:
        for user in usuarios:
            print(f"Nome: {user['nome']}, Idade: {user['idade']}")

def RemoverUsuario(usuarios):
    nome_remover = input("Digite o nome do usuário que deseja remover: ").lower()
        
    for user in usuarios:
        if user["nome"].lower() == nome_remover:
            usuarios.remove(user)
            
            print(f"Usuário {user['nome']} removido com sucesso.")
        



while True:
    print("selecione uma opção")
    opcao = input("[1]Cadastrar , [2]Buscar, [3]Listar, [4]Remover, [5]Sair: ")


    if opcao == "1": # Cadastrar
        CadastrarUsuario(usuarios)

    elif opcao == "2": # Buscar
        BuscarUsuario(usuarios)

    elif opcao == "3": # Listar
        ListarUsuarios(usuarios)
        
    elif opcao == "4": # Remover
        RemoverUsuario(usuarios)

    elif opcao == "5":# Sair
        print("Sair")
        break
    else:
        print("Opção inválida. Tente novamente")
