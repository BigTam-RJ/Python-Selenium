from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

elements = {
    'url_google': 'https://www.google.com.br/',
    'field': '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input',
    'text': 'roblox.com'
}

def open_site(driver):
    v_url = elements['url_google']
    driver.get(v_url)   # carrega o site solicitado
    driver.implicitly_wait(30) # aguarda por 30s o site carregar

def search(driver):
    """ v_field = driver.find_element_by_xpath(elements['field']) - sintaxe substituído pela sintaxe abaixo """
    v_field = driver.find_element(by=By.XPATH, value=elements['field'])
    v_field.send_keys(elements['text'])
    sleep(2)
    v_field.send_keys(Keys.ENTER)


#--------------------------------------------------------------#
#--------------- INICIALIZAÇÃO PRINCIPAL ----------------------#
#--------------------------------------------------------------#
def setup():
    opt = Options()
    driver = webdriver.Chrome(options = opt)
    return driver

def main():
    driver = setup()
    open_site(driver)
    search(driver)
    breakpoint()
    driver.quit()

if __name__ == "__main__":
    main()
#--------------------------------------------------------------#

