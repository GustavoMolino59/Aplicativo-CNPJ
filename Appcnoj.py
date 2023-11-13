import pandas as pd
import requests
import os
import time

file_path = os.path.abspath('fundoIdosos.xlsx')
df = pd.read_excel("CNPJ.xlsx")
print(df.columns)
for i in range (0,100):
    dado = df["CNPJ"].iloc[i]  # Substitua 'sua_coluna' pelo nome da coluna
    url = 'https://receitaws.com.br/v1/cnpj/' + str(dado)
    response = requests.get(url)
    while response.status_code != 200:
        time.sleep(20)
        response = requests.get(url)
    valor_obtido = response.json()
    Cnpj_temporario = pd.DataFrame([valor_obtido])
    if i == 0:
        CNPJ_ATUAL = pd.DataFrame([valor_obtido])
    else:
        CNPJ_ATUAL = pd.concat([CNPJ_ATUAL, Cnpj_temporario], ignore_index=False)
writer = pd.ExcelWriter('Teste.xlsx', engine='xlsxwriter')
print(CNPJ_ATUAL.iloc[0,0])
CNPJ_ATUAL.to_excel(excel_writer=writer, sheet_name='Plan1', index=True, startrow= 2, )
writer.close()