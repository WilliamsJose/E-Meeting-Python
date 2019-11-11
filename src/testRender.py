import json
f = "./database/db.json"


def main():
	with open(f, "r", encoding="utf8") as fr:
		db = json.loads(fr.read())
	fr.close()

	print("qual sala deseja escolher? ")
	for i, sala in enumerate(db["salas"]):
		print("("+str(i+1)+")", sala["sala"], sala["status"])
	sala = int(input(": ")) - 1
	print(db["salas"][sala]["sala"])

	
main()