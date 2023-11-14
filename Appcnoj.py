import pandas as pd
import requests
import time

planilha = pd.read_csv("FDCA2023.csv", sep=';', encoding='ISO-8859-1')

planilha = planilha.drop(planilha.index[:2])
planilha = planilha.reset_index(drop=True)
planilha.columns = planilha.iloc[0]
planilha = planilha.drop(planilha.index[0])

planilha = planilha.assign(nome='')

for index, row in planilha.iterrows():
    dado = row["CNPJ"]
    url = 'https://receitaws.com.br/v1/cnpj/' + str(dado)
    response = requests.get(url)
    while response.status_code != 200:
        time.sleep(20)
        response = requests.get(url)
    valor_obtido = response.json()
    planilha.at[index, 'nome'] =  valor_obtido.get("nome")

planilha.to_csv("Teste.csv", sep=",", index=False)
