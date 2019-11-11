from datetime import datetime

def main():
  dia = 12
  mes = 11
  ano = 2019
  hora = "12:30"

  strDatetime = str(dia) + "/" + str(mes) + "/" + str(ano) + " " + hora

  #converte strings para o formato datetime
  data = datetime.strptime(strDatetime, "%d/%m/%Y %H:%M")
  print(data)

main()