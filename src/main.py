import json
f = "./db.json"


def main():
    principal()


def principal():
    print("\nBem vindo!")
    print("Qual menu deseja ver? ")
    
    text = "\n1 - Usuário Comum. \n2 - Coordenador. \n3 - Gestor de Recursos. \n0 - Sair \nOpção: "
    opt = int(input(text))

    while opt != 0:
        if opt == 1:
            menuUsuarioComum()
        elif opt == 2:
            menuCoordenador()
        elif opt == 3:
            menuGestorDeRecursos()
        elif opt == 4:
            cadastro()
        elif opt == 5:
            listaUsuarios()
        else:
            print("Opção inválida! Tente novamente.")
        opt = int(input(text))


def menuUsuarioComum():
    print("\n--Usuário--")
    print("O que deseja fazer?")
    
    text = "\n1 - Cadastrar-se. \n2 - Entrar. \n0 - Voltar ao Menu Anterior \nOpção: "
    opt = int(input(text))

    while opt != 0:
        if opt == 1:
            cadastro()
        elif opt == 2:
            login()
        elif opt == 3:
            principal()
        else:
            print("\nOpção inválida! Tente novamente.")
        opt = int(input(text))


def menuCoordenador():
    print("\n--Coordenador--")

def menuGestorDeRecursos():
    print("\n--Coordenador--")
            
            
def cadastro():
    nome = input("Digite o Nome: ")
    matricula = input("Digite a Matrícula: ")
    senha = input("Digite a Senha: ")
    pessoa = {"nome": nome, "senha": senha, "matricula": matricula}
    
    # Exceção para caso o arquivo não exista
    try:
        # Lê o arquivo json e salva os valores no array usuarios.
        fr = open(f, "r")
        usuarios = json.loads(fr.read())
        fr.close()
        # Adiciona a nova pessoa no array
        usuarios.append(pessoa)
        # Salva o array atualizado no arquivo
        fw = open(f,"w+")
        fw.write(json.dumps(usuarios, indent=4))
        fw.close()
    except IOError:
        fw = open(f,"w+")
        usuarios = []
        usuarios.append(pessoa)
        fw.write(json.dumps(usuarios, indent=4))
        fw.close()
    
    print("\nCadastro Efetuado!")
    menuUsuarioComum()
                
#Método para testes                
def listaUsuarios():
    with open(f, "r") as fr:
        usuarios = json.loads(fr.read())
    fr.close()

    if usuarios == []:
        print("\nNão há usuários cadastrados.")
    else:
        for user in usuarios:
            print(user["nome"] + "  " + user["matricula"])

#Ler o arquivo
def fileRead():
    with open(f, "r") as fr:
        usuarios = json.loads(fr.read())
    fr.close()
    return usuarios          
            
def login():
    # retorno da leitura do arquivo
    usuarios = fileRead()
    logado = False
    name = input("Usuário: ")
    key = input("Senha: ")

    # Verifica se o que foi digitado é igual ao que tenho guardado
    for user in usuarios:
        if name == user["nome"] and key == user["senha"]:
            print("Bem vindo, " + user["nome"] + "!")
            logado = user
            break

    #apenas para testes
    if logado:
        print(logado)
    else:
        print("Usuário ou senha inválidos")
            
   
        
main()
