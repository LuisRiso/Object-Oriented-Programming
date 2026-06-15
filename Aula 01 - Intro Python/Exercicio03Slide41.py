from datetime import datetime

dataStr = input("Informe a data (dd/yy/yyyy): ")
data = datetime.strptime(dataStr, "%d/%m/%Y")
print(data.weekday())