import json
import os
from getpass import getpass
from time import sleep
from datetime import datetime
from uuid import uuid1

f = "C:/Users/Williams/Desktop/E-Meeting-Python/database/db.json"

def main():
    clear()
    #Cadastrar o primeiro coordenador e gestor
    db = fileRead()
    coord = {"nome": "Carimbo Miguel", "usuario": "coord", "cpf": "87705427087", "matricula": "72951317522", "telefone": "89220611348", "permissao": "Coordenador", "senha": "321", "reunioesConfirmadas": [], "presencaRequerida": []}
    gest = {"nome": "Brucesfielde Porfírio", "usuario": "gest", "cpf": "78456935130", "matricula": "45261664040", "telefone": "83986444444", "permissao": "Gestor de Recursos", "senha": "321", "reunioesConfirmadas": [], "presencaRequerida": []}
    try:
        jaExisteCoord = 0
        jaExisteGest = 0
        for u in db["usuarios"]:
            if coord["nome"] == u["nome"]:
                jaExisteCoord = 1
            elif gest["nome"] == u["nome"]:
                jaExisteGest = 1

        if jaExisteCoord == 0:     
            db["usuarios"].append(coord)
        if jaExisteGest == 0:
            db["usuarios"].append(gest)
    except KeyError:
        db["usuarios"] = []
        db["usuarios"].append(coord)
        db["usuarios"].append(gest)
    finally:
        fileWrite(db)

    #Finalmente inicia o programa para o usuario
    principal()

# <Telas>
def principal():
    message("Seja bem vindo! entre ou cadastre-se.")

    text = "\n(1) Entrar. \n(2) Cadastrar-se. \n(0) Sair \n: "
    opt = input(text)

    if opt == "1":
        login()
    elif opt == "2":
        cadastroComum("Comum")
    elif opt == "0":
        exitProgram()
    else:
        message("Opção inválida! Tente novamente.")
        principal()

def usuarioComumLogado(u):
    message("-----Tela usuário comum----- \nO que deseja fazer hoje?")
    
    opt = input("(1) Cadastrar nova Reunião \n(2) Confirmar ou Negar presença \n(3) Reuniões confirmadas \n(4) Atas \n(0) Sair \n: ")

    if opt == "1":
        cadastrarReuniao(u)
    elif opt == "2":
        presencaRequerida(u)
    elif opt == "3":
        message("reunioesConfirmadas()") #temp
        usuarioComumLogado(u)
    elif opt == "4":
        message("atas()") #temp
        usuarioComumLogado(u)
    elif opt == "0":
        exitProgram()
    else:
        message("Opção inválida! Tente novamente.")
        usuarioComumLogado(u)

def coordenadorLogado(u):
    message("-----Tela Coordenador-----")

    opt = input("(1) Criar reunião \n(2) Editar atas \n(3) Realocar reunião \n(4) Confirmar ou Negar presença \n(5) Reuniões confirmadas \n(0) Sair \n: ")

    if opt == "1":
        cadastrarReuniao(u)
    elif opt == "2":
        message("editarAta()") #temp
        coordenadorLogado(u)
    elif opt == "3":
        message("realocarReuniao()") #temp
        coordenadorLogado(u)
    elif opt == "4":
        message("presencaRequerida()") #temp
        coordenadorLogado(u)
    elif opt == "5":
        message("reunioesConfirmadas()") #temp
        coordenadorLogado(u)
    elif opt == "0":
        exitProgram()
    else:
        message("Opção inválida! Tente novamente.")
        coordenadorLogado(u)

def gestorLogado(u):
    message("-----Tela Gestor-----")

    opt = input("(1) Cadastrar novo espaço \n(2) Confirmar local de Reunião \n(0) Sair \n: ")

    if opt == "1":
        cadNovoEspaco(u)
    elif opt == "2":
        message("confirmarReuniao()") #temp
        gestorLogado(u)
    elif opt == "0":
        exitProgram()
    else:
        message("Opção inválida! Tente novamente.")
        gestorLogado(u)
    
# </Telas>

# <Métodos>
def clear():
    os.system("cls || clear")

# Lê o arquivo
def fileRead():
    try:        
        with open(f, "r", encoding="utf8") as fr:
            db = json.loads(fr.read())
        fr.close()
        return db
    except IOError:
        print("Erro na leitura do arquivo. " + str(IOError))

# Escreve no arquivo
def fileWrite(db):
    try:
        with open(f, "w+", encoding="utf8") as fw:
            fw.write(json.dumps(db, ensure_ascii=False, indent=4))
        fw.close()
    except IOError:
        print("Erro na gravação do arquivo. " + str(IOError))

def welcome(nome):
    clear()
    print(f"Bem vindo(a), {nome} !")
    sleep(1.5)

def exitProgram():
    clear()
    print("Goodbye!")
    sleep(1.5)
    clear()
    exit()

def message(msg):
    clear()
    print(msg)
    sleep(1.5)

def cadastroComum(permissao):
    clear()
    db = fileRead()

    nome = input("Digite seu nome completo: ")

    usuario = input("Digite seu usuario: ")
    # Verifica se usuario já existe
    usuarioVerificado = False
    while usuarioVerificado == False:
        for usuarioDB in db["usuarios"]:
            if usuario == usuarioDB["usuario"]:
                message("Esse usuário já existe, por favor tente outro.")
                usuario = input("Digite seu usuario: ")
                usuarioVerificado = False
            else:
                usuarioVerificado = True

    cpf = input("Digite seu CPF: ")
    matricula = input("Digite sua Matrícula: ")
    telefone = input("Digite seu Telefone: ")
    senha = getpass("Digite a Senha: ")
    confirmaSenha = getpass("Confirme a Senha: ")

    # Verifica se as senhas são iguais
    senhaVerificada = False
    while senhaVerificada == False:
        if senha == confirmaSenha:
            #dados do usuario a cadastrar
            pessoa = {"nome": nome, "usuario": usuario, "cpf": cpf, "matricula": matricula,
                      "telefone": telefone, "permissao": permissao, "senha": senha, "reunioesProprietario": [], "reunioesConfirmadas": [], "presencaRequerida": []}
            senhaVerificada = True
        else:
            message("Senhas devem ser iguais!\n")
            clear()
            print(f"Digite seu nome completo: {nome} \nDigite seu usuario: {usuario} \nDigite seu CPF: {cpf} \nDigite sua Matrícula: {matricula} \nDigite seu Telefone: {telefone}")
            senha = getpass("Digite a Senha: ")
            confirmaSenha = getpass("Confirme a Senha: ")

    # Exceção para caso não exista nenhum usuario
    try:
        db["usuarios"].append(pessoa)
    except KeyError:
        db["usuarios"] = []
        db["usuarios"].append(pessoa)
    finally:
        # Salva o db atualizado no arquivo
        fileWrite(db)
        message("\nCadastro efetuado com sucesso!")
        principal()

def login():
    clear()
    # retorno da leitura do arquivo
    db = fileRead()
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")

    # Verifica o tipo  de usuario e se o que foi digitado é igual ao que tenho guardado
    for usuarioDB in db["usuarios"]:
        if usuarioDB["usuario"] == usuario and senha == usuarioDB["senha"]:
            if usuarioDB["permissao"] == "Comum":
                welcome(usuarioDB["nome"])
                usuarioComumLogado(usuarioDB)
                break
            elif usuarioDB["permissao"] == "Coordenador":
                welcome(usuarioDB["nome"])
                coordenadorLogado(usuarioDB)
                break
            elif usuarioDB["permissao"] == "Gestor de Recursos":
                welcome(usuarioDB["nome"])
                gestorLogado(usuarioDB)
                break
    else:
        message("Usuário ou Senha inválidos")
        principal()

def cadastrarReuniao(u):
    clear()
    # uso o usuario logado para ver quem criou a reunião
    usuarioLogado = u

    db = fileRead()

    def voltaAoInicioLogado():
        if usuarioLogado["permissao"] == "Comum":
            usuarioComumLogado(usuarioLogado)
        elif usuarioLogado["permissao"] == "Coordenador":
            coordenadorLogado(usuarioLogado)
        else:
            gestorLogado(usuarioLogado)

    # caso ainda não tenha ao menos uma sala cadastrada no banco, para o programa e retorna ao inicio
    try:
        db["salas"]
    except KeyError:
        message("Ainda não há salas cadastradas, peça ao gestor de recursos para cadastrar uma nova")
        voltaAoInicioLogado()

    # pega datahora atual e gera um id único
    dataCadastro = datetime.now().strftime("%d/%m/%Y %H:%M")
    idReuniao = str(uuid1())

    tema = input("Tema da reunião ou ata \n:")
    clear()
    
    # renderiza todas as salas de acordo com o banco, permite que o usuário escolha uma e verifica se está ocupada
    while True:
        message("\nQual sala deseja escolher? ")
        for i, sala in enumerate(db["salas"]):
            print("(" + str(i + 1) + ")", sala["sala"], sala["status"])

        sala = input(": ")

        try:
            sala = int(sala) - 1
            if db["salas"][sala]["status"] == "Ocupada":
                message("\nEsta sala está ocupada, por favor escolha outra")
            else:
                break
        except ValueError as e:
            message(f"Erro: {e}, por favor digite um número.")
            sleep(1.5)
    
    message("Sala escolhida: " + db["salas"][sala]["sala"])
    clear()

    data = input("\nDigite a data que será realizada no formato '03/08/2019' \n:")
    clear()

    horasInicio = input("\nDigite o horário de inicio no formato '21:00' \n:")
    clear()

    horasFim = input("\nDigite o horário de fim no formato '21:00' \n:")
    clear()

    ata = input("\nRedija sua ata \n:")
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
            pUsuario = input("Digite o Usuário do participante: ")

            #procura o participante no banco
            for p in db["usuarios"]:
                if p["usuario"] == pUsuario:
                    participante = {"nome": p["nome"], "usuario": p["usuario"], "telefone": p["telefone"]}
                    participantes.append(participante)

                    # "notificando" o participante
                    try:
                        p["presencaRequerida"].append(idReuniao)
                    except KeyError:
                        p["presencaRequerida"] = []
                        p["presencaRequerida"].append(idReuniao)

                    message(f"Participante {p['nome']} adicionado.")
                    break
            else:
                message("Este participante não existe.")

    # dict, object, json, já não sei mais como chamar isso...
    reuniao = {
        "id": idReuniao,
        "tema": tema,
        "ata": ata,
        "sala": db["salas"][sala]["sala"],
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "dataDeCadastro": dataCadastro,
        "criadoPor": usuarioLogado["nome"],
        "participantes": participantes
    }

    #defino o status da sala escolhida como Ocupada
    db["salas"][sala]["status"] = "Ocupada"

    # guardando o id da reunião a ser cadastrada no usuario criador
    for obj in db["usuarios"]:
        if obj["usuario"] == usuarioLogado["usuario"]:
            obj["reunioesProprietario"].append(idReuniao)

    # Exceção caso não exista nenhuma reunião
    try:
        db["reunioes"].append(reuniao)
    except KeyError:
        db["reunioes"] = []
        db["reunioes"].append(reuniao)
    finally:
        fileWrite(db)
        message("Reunião cadastrada com êxito! ")
        
        # volta a tela do usuario que está logado
        voltaAoInicioLogado()
    
def cadNovoEspaco(u):
    clear()
    usuarioLogado = u

    db = fileRead()

    sala = input("Nome da sala \n: ")
    clear()

    while True:
        clear()

        disponivel = input("A sala já está disponível? [S/N] \n: ").upper()
        clear()

        if disponivel == "S":
            status = "Disponível"
            break
        elif disponivel == "N":
            status = "Ocupada"
            break
        else:
            message("Opção inválida! Tente novamente.")

    novoEspaco = {
        "sala": sala,
        "status": status
    }

    try:
        db["salas"].append(novoEspaco)
    except KeyError:
        db["salas"] = []
        db["salas"].append(novoEspaco)
    finally:
        clear()
        fileWrite(db)
        print("Novo espaço cadastrado com sucesso!")
        sleep(1.5)
        gestorLogado(usuarioLogado)

def presencaRequerida(u):
    usuarioLogado = u

    db = fileRead()

    # obtém a reposta do usuário se vai partipar ou não da reunião escolhida
    def decisao(r):
        clear()
        resp = input("Deseja participar dessa reunião? [S/N]").upper()
        
        if resp == "S":
            definePresenca("Sim", r)
        elif resp == "N":
            definePresenca("Não", r)

    # tentativa sem sucesso de mudar o status do participante para "sim" ou "não" na escolha de participar
    def definePresenca(simOuNao, r):
        for reuniao in db["reunioes"]:
            if r["id"] == reuniao["id"]:
                for p in reuniao["participantes"]:
                    if usuarioLogado["usuario"] == p["usuario"]:
                        p["comparecera"] = simOuNao
                        message("Sucesso!")

    def prMain():
        # o try except aqui serve para verificar se a chave existe ou não no usuário atual
        try:
            clear()
            while True:
                reunioes = []

                # mostra as reuniões para o usuário escolher qual vai responder participar ou não
                for i, reuniaoID in enumerate(usuarioLogado["presencaRequerida"]):
                    for reuniao in db["reunioes"]:
                        if reuniaoID == reuniao["id"]:
                            print(f"Tema: {reuniao['tema']}"
                            +f"\nData: {reuniao['dataInicio']} - {reuniao['dataFim']}"
                            +f"\nCriador: {reuniao['criadoPor']}"
                            +f"\n({i + 1}) Escolher esta reunião\n")

                            reunioes.append(reuniao)
                else:
                    if usuarioLogado["presencaRequerida"] == []:
                        message("Você não tem nenhuma reunião pendente.")
                        break
                    print("(0) Voltar")

                opcao = input(": ")


                try:
                    opcao = int(opcao) - 1
                    if opcao != -1:
                        decisao(reunioes[opcao])
                        break
                    else:
                        usuarioComumLogado(usuarioLogado)
                except ValueError as e:
                    message(f"Erro: {e}, por favor digite um número.")
                    sleep(1.5)
        except KeyError:
            message("Você não tem nenhuma reunião pendente.")
        finally:
            usuarioComumLogado(usuarioLogado)
    
    prMain()
    
# def reunioesConfirmadas(u):

# def editarAta(u):

# def realocarReuniao():

# </Métodos>

main()
