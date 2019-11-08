import json
f = "./Database/db.json"

def main():
  with open(f, "r") as fr:
    db = json.loads(fr.read())
    fr.close
  
  print(db["usuarios"])

main()
