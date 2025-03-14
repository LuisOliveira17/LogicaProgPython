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
    resposta=int(input("O que deseja fazer:"))
    if resposta==1:
        CadastroUsuario()
    if resposta==2:
        LoginUsuario()


MenuPrincipal()
