import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialize o driver do Chrome
driver = webdriver.Chrome()

# Abra o site alvo
driver.get("https://ww3.fepam.rs.gov.br/licenciamento/area3/listaRazao.asp?area=3&buscar=2&tipoBusca=municipio&municipio=9999999&razao=&ramo=4751,30")

file = open("crawl.txt", "w")

file.write("RAZAO SOCIAL\tCPF/CNPJ\tENDERECO\tMUNICIPIO EMPREENDEDOR\tBAIRRO\tMUNICIPIO EMPREENDIMENTO\tULTIMA LICENCA\n")

page = 1

print("START")
try:

    while True:
        time.sleep(3)
        print("START PAGE ", page)    

        #SELECIONA TODOS OS DIVS DE ITEM
        div_elements = driver.find_elements(By.CLASS_NAME, "item")
        for div in div_elements:
            #print("START DIV")

            line = ""

            #SELECIONA TODOS OS ITENS DE LISTA
            li_elements = div.find_elements(By.TAG_NAME, "li")
            
            for li in li_elements:
                if li.get_attribute("class") == "dir":
                    line = line + li.text + "\t"
                    #print(li.text)
            line = line.strip()
            line = line + "\n"
            #print(line)
            file.write(line)
            #print("FINISH DIV")
            file.flush()
        print("FINISH PAGE")

        #PROXIMA PAGINA
        btn = driver.find_element(By.ID, "R")
        img_name = os.path.basename(btn.get_attribute("src"))
        #print(img_name)
        #VERIFICA PAGINACAO ATIVA
        if img_name == "paginacao_proxima.gif":
            page += 1
            btn.click()
            #time.sleep(5)
        else:
            break
    
except Exception as e:
    print(f"Erro: {str(e)}")
finally:
    driver.quit()
    file.close()

print("FINISH")
