# Importando bibliotecas
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from dados import importar_dados, cnpjs

# Importando dados
importar_dados()

# Abrindo o navegador
driver = webdriver.Chrome()

# Site que será aberto
url = 'https://www.portaldadrogaria.com.br/11v1'

# Tempo de espera
driver.implicitly_wait(3)

# Maximizando o navegador
driver.maximize_window()

# Abrindo o site
driver.get(url)

# STATUS:
mensagens = []

# Enviando dados
for cnpj in cnpjs:
    # Digitando CNPJ
    campo_cnpj = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[1]/input')
    campo_usuario = driver.find_element(By.ID, 'username')
    campo_inscreva_se = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[5]/div[1]/a')
    campo_cnpj.send_keys(cnpj)

    # Digitando usuário
    campo_usuario.send_keys('asdasd')

    # Clicando em inscreva-se
    campo_inscreva_se.click()

    # Aguardando as informações serem carregadas
    time.sleep(3)

    try:
        span = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/p').text
        if span == 'QT49 - Reconhecemos como Matriz o primeiro CNPJ da Rede, ou seja como Sufixo 0001-XX. Realize a inscrição com o CNPJ da Matriz':
            print(f'{cnpj} não cadastrado.')
            mensagens.append('NÃO CADASTRADO')
    except:
        pass

    try:
        span = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/p[2]').text
        if span == 'Para realizar o cadastro da sua loja, acesse o Portal da Drogaria com o CNPJ da Matriz. ':
            print(f'{cnpj} não cadastrado.')
            mensagens.append('NÃO CADASTRADO')
    except:
        pass

    driver.refresh()
    time.sleep(3)
