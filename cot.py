from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()

#entrando no site
driver.get('https://www.melhorcambio.com/dolar-hoje')
#procurando o preço do dólar pelo xpath
cot_dolar = driver.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')

#entrando no site
driver.get('https://www.melhorcambio.com/euro-hoje')
#procurando o preço do euro pelo xpath
cot_euro = driver.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')

#fechando o site
driver.quit()

#informações da tabela
cots = {'Moeda': ['Dólar', 'Euro'],
        'Converção': [cot_dolar, cot_euro],}

#montando a tabela
tabCot = pd.DataFrame(cots)

display(tabCot)
