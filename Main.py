import json



def CarregarUsuarios():
     try:
          with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
     except FileNotFoundError:
                return []

usuarios = CarregarUsuarios()

def SalvarUsuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def CadastrarUsuario(usuarios):
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))

    usuario = {
            "nome": nome, 
            "idade": idade
        }

    usuarios.append(usuario)
    SalvarUsuarios(usuarios)
        
    print("usario cadastrado com sucesso!")

def BuscarUsuario(usuarios):
    busca = input("Digite o nome do usuário que deseja buscar: ").lower().strip()
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
    nome_remover = input("Digite o nome do usuário que deseja remover: ").lower().strip()
        
    for user in usuarios:


        if user["nome"].lower() == nome_remover:
            usuarios.remove(user)
            SalvarUsuarios(usuarios)
            print(f"Usuário {user['nome']} removido com sucesso.")
            return
        
    print("Usuário não encontrado.")
        



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
