import json
from getpass import getpass
import os
from time import sleep
f = "./database/db.json"


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
    db = fileRead()

    nome = input("Digite seu nome completo: ")

    usuario = input("Digite seu usuario: ")
    # Verifica se usuario já existe
    usuarioVerificado = False
    while usuarioVerificado == False:
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"]:
                print("Esse usuário já existe, tente outro.")
                usuario = input("Digite seu usuario: ")
                usuarioVerificado = False
            else:
                usuarioVerificado = True

    cpf = input("Digite seu CPF: ")
    matricula = input("Digite sua Matrícula: ")
    telefone = input("Digite seu Telefone: ")
    senha = getpass("Digite a Senha: ")
    confirmaSenha = getpass("Confirme a Senha: ")
    permissao = "Comum"

    # Verifica se as senhas são iguais
    senhaVerificada = False
    while senhaVerificada == False:
        if senha == confirmaSenha:
            #dados do usuario a cadastrar
            pessoa = {"nome": nome, "usuario": usuario, "cpf": cpf, "matricula": matricula,
                      "telefone": telefone, "permissao": permissao, "senha": senha, "reunioesProprietario": [], "reunioesConfirmadas": []}
            senhaVerificada = True
        else:
            clear()
            print("Senhas devem ser iguais!\n")
            print("Digite seu nome completo: ", nome, "\nDigite seu usuario: ", usuario, "\nDigite seu CPF: ", cpf,
                  "\nDigite sua Matrícula: ", matricula, "\nDigite seu Telefone: ", telefone)
            senha = getpass("Digite a Senha: ")
            confirmaSenha = getpass("Confirme a Senha: ")

    # Exceção para caso o arquivo não exista
    try:
        db["usuarios"].append(pessoa)
    except IOError:
        db["usuarios"] = []
        db["usuarios"].append(pessoa)
    finally:
        # Salva o db atualizado no arquivo
        fw = open(f, "w+", encoding="utf-8")
        fw.write(json.dumps(db, ensure_ascii=False, indent=4))
        fw.close()

    print("\nCadastro Efetuado!")
    sleep(2)
    menuUsuarioComum()


# Lê o arquivo
def fileRead():
    with open(f, "r", encoding="utf-8") as fr:
        db = json.loads(fr.read())
    fr.close()
    return db


def login(permissao):
    # retorno da leitura do arquivo
    db = fileRead()
    usuarioLogado = False
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")

    # Verifica o tipo  de usuario e se o que foi digitado é igual ao que tenho guardado
    if permissao == "Comum":
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"] and senha == usuarioDB["senha"]:
                print("Bem vindo, " + usuarioDB["nome"] + "!")
                usuarioLogado = usuarioDB
                break
    elif permissao == "Coordenador" or permissao == "Gestor de Recursos":
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"] and senha == usuarioDB["senha"] and permissao == usuarioDB["permissao"]:
                print("Bem vindo, " + usuarioDB["nome"] + "!")
                usuarioLogado = usuarioDB
                break

    if usuarioLogado:
        print(usuarioLogado)
    else:
        print("Usuário ou Senha Inválidos")
        sleep(2)
        principal()


main()
