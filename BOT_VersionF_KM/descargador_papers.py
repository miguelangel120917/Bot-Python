import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import busqueda
from datetime import datetime, timedelta

main_search = busqueda.val_busqueda_input
libro = ''#busqueda.val_journal_input
autor = busqueda.val_autor_input
main_search2 = main_search.replace(':','').replace('\\','').replace('/','').replace('*','').replace('?','').replace('"','\'').replace('<','(').replace('>',')').replace('|','l')

try:
    os.mkdir(main_search)
except FileExistsError:
    print("creado")

driver = webdriver.Chrome()
driver.get('https://www.sciencedirect.com/search')
driver.find_element_by_id('qs-searchbox-input').send_keys(main_search)
driver.find_element_by_id('authors-searchbox-input').send_keys(autor)
driver.find_element_by_id('pub-searchbox-input').send_keys(libro)
driver.find_element_by_id('volume-searchbox-input').send_keys('')
driver.find_element_by_id('issue-searchbox-input').send_keys('')
driver.find_element_by_id('page-searchbox-input').send_keys('')

driver.find_element_by_id('qs-searchbox-input').send_keys(Keys.RETURN)
time.sleep(4)

driver.find_element_by_css_selector("button[class='button modal-close-button button-anchor move-right move-top u-margin-s size-xs']").click()
li_list = driver.find_elements_by_xpath('//li[@data-doi]')

doi_list = []
for li in li_list:
    doi_list.append(li.get_attribute('data-doi'))

a_list = driver.find_elements_by_xpath('//li[@data-doi]//h2/a')
nombres_list = []
for a in a_list:
    nombres_list.append(a.text.replace(':','').replace('\\','').replace('/','').replace('*','').replace('?','').replace('"','\'').replace('<','(').replace('>',')').replace('|','l'))

driver.close()


num=0
num2=0
flag_descargado = []
for i, doi in enumerate(doi_list):
    r = requests.get('https://sci-hub.tw/'+doi)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    try:
        # if html_body.find()
        pdf_link = html_soup.find(id='article').iframe.get('src').split('#view')[0] 
        if pdf_link[:2] == '//':
            pdf_link = 'http:' + pdf_link
        with open(main_search+'/'+nombres_list[i]+'.pdf', 'wb') as f:
            #print(nose+'/'+nombres_list[i]+'.pdf')
            #print(pdf_link)
            f.write(requests.get(pdf_link).content)
        print('Descargado el paper ',str(i))
        flag_descargado.append('downloaded')
        num=num+1
    except (AttributeError,ConnectionError):
        flag_descargado.append('failed')
        num2=num2+1
    except UnicodeEncodeError:
        flag_descargado.append('failed')
        num2=num2+1

historic_file = open("historico.txt","a")
historic_file.write(main_search2+' LISTA DE PAPERS:'+'\t'+'STATUS'+'\t'+'FECHA'+'\t'+'DOI'+'\n')
for i, k in enumerate(nombres_list):
    historic_file.write(k+'\t'+flag_descargado[i]+'\t'+datetime.now().strftime("%Y/%m/%d, %H:%M:%S")+'\t'+doi_list[i]+'\n')

historic_file.write('FIN DE BUSQUEDA '+main_search2+'\t'+str(num)+' PAPERS DESCARGADOS'+'\t'+str(num2)+' PAPERS NO DISPONIBLES'+'\t'+'TEMA: '+main_search+'\r\n')
historic_file.close()

validation_file = open("validador.py","w+")
validation_file.write("val_busqueda = '"+main_search2+'\'')
validation_file.close()
        
# si no encuentra el paper en scihub
#si esta siendo usado cerrarlo PermissionError