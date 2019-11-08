import json
from getpass import getpass
import os
from time import sleep
f = "./Database/db.json"

def main():
    clear()
    principal()



def clear():
    os.system("cls")



def principal():
    clear()
    print("Bem vindo!")
    print("Qual menu deseja ver? ")
    
    text = "\n1 - Usuário Comum. \n2 - Coordenador. \n3 - Gestor de Recursos. \n0 - Sair \nOpção: "
    opt = int(input(text))

    if opt == 1:
        menuUsuarioComum()
    elif opt == 2:
        menuCoordenador()
    elif opt == 3:
        menuGestorDeRecursos()
    elif opt == 4:
        cadastroComum()
    elif opt == 5:
        listaUsuarios()
    elif opt == 0:
        clear()
        print("Goodbye!")
        sleep(1)
        clear()
        exit
    else:
        print("\nOpção inválida! Tente novamente.")
        sleep(1)
        principal()
    


def menuUsuarioComum():
    clear()
    print("--Usuário--")
    print("Faça login ou Cadastre-se")
    
    text = "\n1 - Cadastrar-se. \n2 - Entrar. \n0 - Voltar ao Menu Anterior \nOpção: "
    opt = int(input(text))

    if opt == 1:
        cadastroComum()
    elif opt == 2:
        login("Comum")
    elif opt == 0:
        principal()
    else:
        print("\nOpção inválida! Tente novamente.")
        sleep(1.5)
        menuUsuarioComum()



def menuCoordenador():
    clear()
    print("--Coordenador--")
    text = "1 - Entrar. \n0 - Voltar ao Menu Anterior. \nOpção: "

    opt = int(input(text))

    if opt == 1:
        login("Coordenador")
    elif opt == 0:
        principal()
    else:
        print("\nOpção inválida, Tente novamente.")
        sleep(1)
        menuCoordenador()



def menuGestorDeRecursos():
    clear()
    print("--Gestor de Recursos--")
    text = "1 - Entrar. \n0 - Voltar ao Menu Anterior. \nOpção: "

    opt = int(input(text))

    if opt == 1:
        login("Gestor de Recursos")
    elif opt == 0:
        principal()
    else:
        print("\nOpção inválida, Tente novamente.")
        sleep(1)
        menuGestorDeRecursos()



            
def cadastroComum():
    clear()
    nome = input("Digite seu Nome: ")
    cpf = input("Digite seu CPF: ")
    matricula = input("Digite sua Matrícula: ")
    telefone = input("Digite seu Telefone: ")
    senha = getpass("Digite a Senha: ")
    confirmaSenha = getpass("Confirme a Senha: ")
    permissao = "Comum"

    # Verifica se as senhas são iguais
    ok = False
    while ok == False:
        if senha == confirmaSenha:
            pessoa = {"nome":nome, "cpf":cpf, "matricula":matricula, "telefone":telefone, "permissao":permissao, "senha":senha}
            ok = True
        else:
            clear()
            print("Senhas devem ser iguais!\n")
            print("Digite seu Nome:",nome,"\nDigite seu CPF:",cpf,"\nDigite sua Matrícula:",matricula,"\nDigite seu Telefone:", telefone)
            senha = getpass("Digite a Senha: ")
            confirmaSenha = getpass("Confirme a Senha: ")
    
    # Exceção para caso o arquivo não exista
    try:
        # Lê o arquivo json e salva os valores no array usuarios.
        db = fileRead()
        # Adiciona a nova pessoa no array
        db["usuarios"].append(pessoa)
        # Salva o array atualizado no arquivo
        fw = open(f,"w+")
        fw.write(json.dumps(db, indent=4))
        fw.close()
    except IOError:
        fw = open(f,"w+")
        db["usuarios"] = []
        db["usuarios"].append(pessoa)
        fw.write(json.dumps(db, indent=4))
        fw.close()
    
    print("\nCadastro Efetuado!")
    sleep(2)
    menuUsuarioComum()



#Método para testes                
def listaUsuarios():
    clear()
    with open(f, "r") as fr:
        db = json.loads(fr.read())
    fr.close()

    if db == []:
        print("\nNão há usuários cadastrados.")
    else:
        for user in db["usuarios"]:
            print(user["nome"] + "  " + user["matricula"])



#Ler o arquivo
def fileRead():
    with open(f, "r") as fr:
        db = json.loads(fr.read())
    fr.close()
    return db          




def login(permissao):
    # retorno da leitura do arquivo
    db = fileRead()
    logado = False
    name = input("Usuário: ")
    key = getpass("Senha: ")

    # Verifica o tipo  de usuario e se o que foi digitado é igual ao que tenho guardado
    if permissao == "Comum":
        for user in db["usuarios"]:
            if name == user["nome"] and key == user["senha"]:
                print("Bem vindo, " + user["nome"] + "!")
                logado = user
                break
    elif permissao == "Coordenador" or permissao == "Gestor de Recursos":
        for user in db["usuarios"]:
            if name == user["nome"] and key == user["senha"] and permissao == user["permissao"]:
                print("Bem vindo, " + user["nome"] + "!")
                logado = user
                break
        

    if logado:
        print(logado)
    else:
        print("Usuário ou Senha Inválidos")
        sleep(2)
        principal()
            
   
        
main()