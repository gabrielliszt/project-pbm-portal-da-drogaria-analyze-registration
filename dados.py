import pandas as pd

cnpjs = []


def importar_dados():
    arquivo = pd.read_excel('C:\\Users\\pbm\\Meu Drive\\Planilhas\\!ATENDIMENTOS - Gabriel.xlsx', dtype=str)

    portal_verificar = arquivo.loc[arquivo['PORTAL DA DROGARIA'] == 'VERIFICAR']

    for valor in portal_verificar['CNPJ']:
        cnpjs.append(valor)
