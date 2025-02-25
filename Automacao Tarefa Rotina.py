from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importando a classe Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Caminho para o ChromeDriver
caminho_chromedriver = 'C:\\Users\\erirodrigues\\Documents\\GitHub\\Python_Pags\\chromedriver.exe'

service = Service(caminho_chromedriver)
navegador = webdriver.Chrome(service=service)

# Maximizar a janela
navegador.maximize_window()

# Acessando o site
navegador.get('https://jiraps.atlassian.net/jira/software/c/projects/MET/boards/37')
time.sleep(10)

login = navegador.find_element(By.ID, "username")
login.send_keys("erirodrigues@uolinc.com")
# Pressiona ENTER para pesquisar
login.send_keys(Keys.RETURN)
time.sleep(10)

login = navegador.find_element(By.NAME, "loginfmt")
login.send_keys("erirodrigues@uolinc.com")
login.send_keys(Keys.RETURN)
time.sleep(5)

login = navegador.find_element(By.NAME, "passwd")
login.send_keys("Eer#2222")
login.send_keys(Keys.RETURN)
time.sleep(20)

login = navegador.find_element(By.ID, "idSIButton9").click()
time.sleep(20)

login = navegador.find_element(By.XPATH, "//*[@id='card-MET-9047']/div[1]/div/div[1]/div/div/div[1]/div/span").click()
time.sleep(10)

texto = navegador.find_element(By.XPATH, "//*[@id='jira']/div[20]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div")
texto.click()
time.sleep(10)

texto = navegador.find_element(By.XPATH, "//*[@id='ak-editor-textarea']")
texto.send_keys("1,06")
texto.send_keys(Keys.ARROW_UP)
time.sleep(10)
