from urllib.request import urlopen
from bs4 import BeautifulSoup

def buscar_faixas(dose_final, bs):
   for dose in range(1, dose_final + 1):
        id_select = f"vPUBLICOALVOVACINAID_D{dose}"
        select = bs.find('select', id=id_select)
        options = select.find_all('option')
        print(f"Vacinação Dose{dose}")
        for option in options:
            if option['value'] != "":    
             print(f"ID: {option['value']} DESCRIÇÃO: {option.text}")
        print("*******************")

html = urlopen("https://vacinacovid.saobernardo.sp.gov.br/VacinaSBCProd/servlet/inicial")
bs = BeautifulSoup(html, 'html.parser')

buscar_faixas(3, bs)  







