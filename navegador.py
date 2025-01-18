from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importando a classe Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Caminho para o ChromeDriver
caminho_chromedriver = 'C:\\Users\\erirodrigues\\Documents\\Python\\chromedriver.exe'

# Inicializando o navegador com o serviço
service = Service(caminho_chromedriver)  # Passando o caminho do ChromeDriver para o Service
navegador = webdriver.Chrome(service=service)

# Maximizar a janela
navegador.maximize_window()

# Acessando o site
navegador.get('https://pagseguro.uol.com.br/')

time.sleep(5)

# acessando login
navegador.find_element(By.XPATH, '//*[@id="lgpd-ps-banner"]/div/div/button').click() # aceitando cookies
navegador.find_element(By.XPATH, '//*[@id="__next"]/header/div/div[2]/div/div/a[1]').click() # acessar conta

# username
login = navegador.find_element(By.XPATH, '//*[@id="user"]')
login.send_keys('')
navegador.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(5)

# inserindo a senha
senha = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/form/input[1]')
senha.send_keys('')
navegador.find_element(By.XPATH, '//*[@id="enter"]').click()
time.sleep(15)

# dentro da conta
navegador.find_element(By.XPATH, '//*[@id="maquininhas"]/div[2]/span').click() # maquininhas
time.sleep(5)
navegador.find_element(By.XPATH, '//*[@id="maquininhas-secao_2"]/a/span').click() # pedir maquininha
time.sleep(3)
navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div/div/div/div[3]/div/div/div[2]/div[2]/a').click() # selecionando minizinha nfc 2
time.sleep(5)
select = Select(navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div/div[2]/div[2]/div/label'))
select.deselect_by_index()

time.sleep(30)
