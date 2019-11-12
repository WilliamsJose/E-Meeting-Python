import json
import os
from getpass import getpass
from time import sleep
from datetime import datetime

f = "./database/db.json"


def main():
    clear()
    principal()


# <Telas>
def principal():
    clear()
    print("Bem vindo!")
    print("Qual menu deseja ver? ")

    text = "\n(1) Usuário Comum. \n(2) Coordenador. \n(3) Gestor de Recursos. \n(0) Sair \n: "
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

    text = "\n(1) Cadastrar-se. \n(2) Entrar. \n(0) Voltar ao Menu Anterior \nOpção: "
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
    text = "(1) Entrar. \n(0) Voltar ao Menu Anterior. \nOpção: "

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
    text = "(1) Entrar. \n(0) Voltar ao Menu Anterior. \nOpção: "

    opt = int(input(text))

    if opt == 1:
        login("Gestor de Recursos")
    elif opt == 0:
        principal()
    else:
        print("\nOpção inválida, Tente novamente.")
        sleep(1)
        menuGestorDeRecursos()


def usuarioComumLogado(u):
    clear()
    print("-----Tela usuário comum----- \nO que deseja fazer hoje?")
    opt = int(input("(1) Cadastrar nova Reunião \n: "))

    if opt == 1:
        cadastrarReuniao(u)


def coordenadorLogado(u):
    clear()
    print("Tela coordenador")


def gestorLogado(u):
    clear()
    print("Tela gestor")

# </Telas>

# <Métodos>
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


# Lê o arquivo
def fileRead():
    with open(f, "r", encoding="utf-8") as fr:
        db = json.loads(fr.read())
    fr.close()
    return db


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


def login(permissao):
    clear()
    # retorno da leitura do arquivo
    db = fileRead()
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")

    # Verifica o tipo  de usuario e se o que foi digitado é igual ao que tenho guardado
    if permissao == "Comum":
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"] and senha == usuarioDB["senha"]:
                print("Bem vindo(a), " + usuarioDB["nome"] + "!")
                sleep(1.5)
                usuarioComumLogado(usuarioDB)
                break
        else:
            print("Usuário ou Senha Inválidos")
            sleep(2)
            principal()

    else:
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"] and senha == usuarioDB["senha"] and permissao == usuarioDB["permissao"]:
                print("Bem vindo(a), " + usuarioDB["nome"] + "!")
                sleep(1.5)
                coordenadorLogado(usuarioDB) if usuarioDB["permissao"] == "Coordenador" else gestorLogado(usuarioDB)
                break
        else:
            print("Usuário ou Senha Inválidos")
            sleep(2)
            principal()


def cadastrarReuniao(u):
    clear()
    # uso o usuario logado para ver quem criou a reunião
    usuarioLogado = u

    with open(f, "r", encoding="utf8") as fr:
        db = json.loads(fr.read())
    fr.close()

    dataCadastro = datetime.now().strftime("%d/%m/%Y %H:%M")

    tema = str(input("Tema da reunião ou ata \n:"))
    clear()
    
    # renderiza todas as salas de acordo com o banco, permite que o usuário escolha uma e verifica se está ocupada
    print("\nQual sala deseja escolher? ")
    for i, sala in enumerate(db["salas"]):
        print("("+str(i+1)+")", sala["sala"], sala["status"])

    sala = int(input(": ")) - 1

    while db["salas"][sala]["status"] == "Ocupada":
        print("Esta sala está ocupada, por favor escolha outra")
        sala = int(input(": ")) - 1
    
    print(db["salas"][sala]["sala"])
    sleep(1)
    clear()

    data = str(input("\nDigite a data que será realizada no formato '03/08/2019' \n:"))
    clear()

    horasInicio = str(input("\nDigite o horário de inicio no formato '21:00' \n:"))
    clear()

    horasFim = str(input("\nDigite o horário de fim no formato '21:00' \n:"))
    clear()

    ata = str(input("\nRedija sua ata \n:"))
    clear()

    dataInicio = data + " " + horasInicio

    dataFim = data + " " + horasFim

    participantes = []

    # adicionando participantes a reunião
    resp = "S"
    while resp == "S":
        clear()
        resp = input("\nDeseja adicionar um participante? [S/N] \n:" if len(participantes) == 0 else "Deseja adicionar mais um participante? [S/N] \n:").upper()
        if resp == "S":
            pCPF = input("Digite o cpf do participante: ")

            #procura o participante no banco
            for p in db["usuarios"]:
                if p["cpf"] == pCPF:
                    participante = {"nome": p["nome"], "cpf": p["cpf"], "telefone": p["telefone"]}
                    participantes.append(participante)
                    print("Participante " + p["nome"] + " adicionado.")
                    sleep(1)
                    break
            else:
                print("Participante não existe.")
                sleep(1)

    # dict, object, json, já não sei mais como chamar isso...
    reuniao = {
        "tema": tema,
        "ata": ata,
        "sala": db["salas"][sala]["sala"],
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "dataDeCadastro": dataCadastro,
        "criadoPor": usuarioLogado["nome"],
        "participantes": participantes
    }

    try:
        db["reunioes"].append(reuniao)
    except IOError:
        db["reunioes"] = []
        db["reunioes"].append(reuniao)
    finally:
        clear()
        print("Reunião cadastrada com êxito! ")

        with open(f, "w+", encoding="utf8") as fw:
            fw.write(json.dumps(db, ensure_ascii=False, indent=4))
        fw.close()

        sleep(1.5)
        
        if usuarioLogado["permissao"] == "Comum":
            usuarioComumLogado(usuarioLogado)
        elif usuarioLogado["permissao"] == "Coordenador":
            coordenadorLogado(usuarioLogado)
        else:
            gestorLogado(usuarioLogado)
    
# </Métodos>

main()
