from datetime import datetime

data_atual = datetime.now()
# print(data_atual)

data_formatada = data_atual.strftime('%d%m%Y')
print(data_formatada)