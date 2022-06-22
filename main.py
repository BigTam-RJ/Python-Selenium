""" Primeiro, Virtualizar o ambiente do projeto
python -m venv .nomePasta """

""" Para acessar a pasta do projeto, digitar no terminal
.\.venv\Scripts\activate """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
""" from selenium.webdriver.common.keys import Keys """
from time import sleep
import json

""" - automation anywehe
    - UIpath
    - Power automate 
clarismilton@hotmail.com """

file = open("dados.json")
data_file = json.load(file)

elements = {
    'url_site': 'http://www.rpachallenge.com/',
    'first_name': '//input[@ ng-reflect-name="labelFirstName"]',
    'last_name': '//input[@ ng-reflect-name="labelLastName"]',
    'address': '//input[@ ng-reflect-name="labelAddress"]',
    'email': '//input[@ ng-reflect-name="labelEmail"]',
    'role': '//input[@ ng-reflect-name="labelRole"]',
    'company': '//input[@ ng-reflect-name="labelCompanyName"]',
    'phone': '//input[@ ng-reflect-name="labelPhone"]',
    'submit': '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input',
    'start': '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button'
}

def setup():
    opt = Options()
    driver = webdriver.Chrome(options = opt)
    return driver

def open_site(driver):
    v_url = elements['url_site']
    driver.get(v_url)   # carrega o site solicitado
    driver.maximize_window()
    driver.implicitly_wait(30) # aguarda por 30s o site carregar

def commands(driver):
    start = driver.find_element(by=By.XPATH,value=elements['start'])

    v_return = start.is_displayed()
    print("Comando Is Displayed ============= ",v_return)

    v_return = driver.title
    print("Comando Title ==================== ",v_return)

    v_return = driver.current_url
    print("Comando Current URL ============== ",v_return)

def fill_form(driver):
    start = driver.find_element(by=By.XPATH,value=elements['start'])
    start.click()
    #sleep(2)

    for ficha in data_file["ficha"]:
        first_name = driver.find_element(by=By.XPATH,value=elements['first_name'])
        first_name.send_keys(ficha['first_name'])
        #sleep(2)
        last_name = driver.find_element(by=By.XPATH,value=elements['last_name'])
        last_name.send_keys(ficha['last_name'])
        #sleep(2)
        address = driver.find_element(by=By.XPATH,value=elements['address'])
        address.send_keys(ficha['address'])
        #sleep(2) 
        email = driver.find_element(by=By.XPATH,value=elements['email'])
        email.send_keys(ficha['email'])
        #sleep(2)
        role = driver.find_element(by=By.XPATH,value=elements['role'])
        role.send_keys(ficha['role'])
        #sleep(2) 
        company = driver.find_element(by=By.XPATH,value=elements['company'])
        company.send_keys(ficha['company'])
        #sleep(2) 
        phone = driver.find_element(by=By.XPATH,value=elements['phone'])
        phone.send_keys(ficha['phone'])
        #sleep(2) 

        submit = driver.find_element(by=By.XPATH,value=elements['submit'])
        submit.click()
        #sleep(2)
    file.close()

#--------------------------------------------------------------#
#--------------- INICIALIZAÇÃO PRINCIPAL ----------------------#
#--------------------------------------------------------------#
def main():
    driver = setup()
    open_site(driver)
    fill_form(driver)
    commands(driver)
    breakpoint()
    driver.quit()

if __name__ == "__main__":
    main()
#--------------------------------------------------------------#