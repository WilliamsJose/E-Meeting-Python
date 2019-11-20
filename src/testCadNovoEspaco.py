f = "./database/db.json"
import json
from time import sleep
import os

def clear():
    os.system("cls || clear")

def cadNovoEspaco2():

    with open(f, "r", encoding="utf8") as fr:
        db = json.loads(fr.read())
    fr.close()

    sala = input("Nome da sala \n: ")
    clear()

    disponivel = input("A sala já está disponível? [S/N] \n: ").upper()
    clear()

    if disponivel == "S":
        status = "Disponível"
    else:
        status = "Ocupada"

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
        
        with open(f, "w+", encoding="utf8") as fw:
            fw.write(json.dumps(db, ensure_ascii=False, indent=4))
        fw.close()

        print("Novo espaço cadastrado com sucesso!")
        sleep(1.5)
        cadNovoEspaco2()

cadNovoEspaco2()