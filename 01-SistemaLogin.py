usuario={}

def LoginUsuario():
    userLogin=input("Digite seu usuário de entrada:")
    userSenha=int(input("Digite sua senha:"))

    for key, value in usuario.items():
        if key == userLogin and value == userSenha:
            print("Seja bem-vindo!!!!!")
        
        else:
            print("Usuário incorreto")
               
            

def CadastroUsuario():
    user=input("Digite seu nome:")
    senha=int(input("Digite sua senha:"))
    usuario[user] = senha
    print("Cadastro realizado com sucesso")
    print(usuario)
    MenuPrincipal()
    
def MenuPrincipal():
    print("---Menu Principal---")
    print("|1-Cadastrar Usuario|")
    print("|2-Login de Usuario |")
    print("|3-Sair             |")
    print("|-------------------|")

MenuPrincipal()
while True:
    resposta = int(input("Digite 1, 2 ou 3 para continuar (Digite 3 para sair): "))
    
    if resposta == 3:
        print("Saindo...")
        break  # Sai do loop quando a resposta for 3
    elif resposta == 1:
        print("Você escolheu 1!")
    elif resposta == 2:
        print("Você escolheu 2!")
    else:
        print("Opção inválida! Tente novamente.")

MenuPrincipal()
