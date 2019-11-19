from uuid import uuid1

arr = []
id2 = []

# preenchendo array com objs e id2 com os ids gerados
for i in range(3):
    id = str(uuid1())
    id2.append(id)
    arr.append({"id": id, "nome": "Williams", "telefone": 986344223})

print("arr: " + str(arr))
print("id2 a buscar: " + str(id2[0]))

# obj recebe o objeto do arr equivalente ao id2 que busquei
for indice, objeto in enumerate(arr):
    if objeto["id"] == id2[0]:
        obj = objeto

print("obj: " + str(obj))