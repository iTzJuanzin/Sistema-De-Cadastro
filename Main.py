usuarios = []

while True:
    print("selecione uma opção")
    opcao = input("[1]Cadastrar , [2]Buscar, [3]Listar, [4]Remover, [5]Sair: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        usuario = {
            "nome": nome, 
            "idade": idade
        }

        usuarios.append(usuario)
        
        print("usario cadastrado com sucesso!")


    elif opcao == "2":
        busca = input("Digite o nome do usuário que deseja buscar: ").lower()
        encontrado = False

        for user in usuarios:
            if user['nome'].lower() == busca:
                print(f"Usuário encontrado: Nome: {user['nome']}, Idade: {user['idade']}")
                encontrado = True
                
        if not encontrado:
            print("Usuário não encontrado.")

        

    elif opcao == "3":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for user in usuarios:
                print(f"Nome: {user['nome']}, Idade: {user['idade']}")
        


    elif opcao == "4":
        print("Remover")
    elif opcao == "5":
        print("Sair")
        break
    else:
        print("Opção inválida. Tente novamente")
