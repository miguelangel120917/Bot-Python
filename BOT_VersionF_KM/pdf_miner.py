# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:13:42 2019

@author: jorellanau
"""

import PyPDF2
import validador
import os
import time
for pdf in os.listdir(path=validador.val_busqueda):
    pdf_file = open('D:/Trasladar/Python/Proyecto/Tarea/'+validador.val_busqueda+'/'+pdf,'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    cont = 0
    for i in range(number_of_pages):
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        #apariciones = page_content.upper().count(validador.val_busqueda.upper())
        #cont = cont+apariciones
    #print ("validacion del pdf "+pdf+": \n "+"Número de páginas: "+str(number_of_pages)+"\n"+"Número de apariciones: "+str(apariciones))
    print ("validacion del pdf "+pdf+": \n "+"Número de páginas: "+str(number_of_pages))
time.sleep(100)
wait = input("PRESS ENTER TO CONTINUE.")
#pdf_file2 = open('D:/Trasladar/Python/Proyecto/Tarea/'+validador.val_busqueda+'/getBackgroundReport.pdf','rb')
#read_pdf = PyPDF2.PdfFileReader(pdf_file2)
#page2 = read_pdf.getPage(0)
#page_content = page2.extractText()
#
#
#
#number_of_pages = read_pdf.getNumPages()
#page = read_pdf.getPage(0)
#page_content = page.extractText()
#print (page_content)
#page_content.split()
#File_object = open(r"File_Name","Access_Mode")
#File_object.write(str1)
#File_object.writelines(L) for L = [str1, str2, str3]
#file_object.close()
#print(page_content.split().index('JULIO'))
#print(page_content.split().index('JULIOS'))
