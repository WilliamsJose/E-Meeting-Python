import json
import re
from datetime import datetime

f = "./database/db.json"

#falta relacionar usuario com a sua reunião
#falta verificar se a sala está ocupada nos horários
def cadReuniao(usuario):
    usuarioLogado = usuario
    with open(f, "r", encoding="utf8") as fr:
        db = json.loads(fr.read())
    fr.close()

    dataCadastro = datetime.now().strftime("%d/%m/%Y %H:%M")
    tema = str(input("Tema da reunião ou ata:\n"))
    
    #renderiza todas as salas de acordo com o banco, e verifica se está ocupada
    print("qual sala deseja escolher? ")
    for i, sala in enumerate(db["salas"]):
        print("("+str(i+1)+")", sala["sala"], sala["status"])

    sala = int(input(": ")) - 1
    while db["salas"][sala]["status"] == "Ocupada":
        print("Esta sala está ocupada, por favor escolha outra: ")
        sala = int(input(": ")) - 1
    print(db["salas"][sala]["sala"])

    data = str(input("Digite a data que será realizada no formato '03/08/2019':\n"))
    horasInicio = str(input("Digite o horário de inicio no formato '21:00':\n"))
    horasFim = str(input("Digite o horário de fim no formato '21:00':\n"))
    ata = str(input("Redija sua ata:\n"))
    dataInicio = data + " " + horasInicio
    dataFim = data + " " + horasFim
    participantes = []

    resp = "S"
    while resp == "S":
        resp = input("Deseja adicionar um participante? [S/N]:\n" if len(participantes) == 0 else "Deseja adicionar mais um participante? [S/N]:\n").upper()
        if resp == "S":
            pCPF = input("Digite o cpf do participante: ")

            #procura o participante no banco
            for p in db["usuarios"]:
                if p["cpf"] == pCPF:
                    participante = {"nome": p["nome"], "cpf": p["cpf"], "telefone": p["telefone"]}
                    participantes.append(participante)
            else:
                print("Participante não existe.")

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
        with open(f, "w+", encoding="utf8") as fw:
            fw.write(json.dumps(db, ensure_ascii=False, indent=4))
        fw.close()

cadReuniao({"nome": "williams"})