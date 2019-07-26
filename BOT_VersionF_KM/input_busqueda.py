# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 01:02:50 2019

@author: jorellanau
"""
#administracion del conocimiento
#administracion
def printtext():
    global e
    string = e.get()
    string2 = f.get()
    string3 = g.get()
    busqueda_file = open("busqueda.py","w+")
    busqueda_file.write("val_busqueda_input = '"+string+'\''+'\n')
    busqueda_file.write("val_journal_input = '"+string2+'\''+'\n')
    busqueda_file.write("val_autor_input = '"+string3+'\''+'\n')
    busqueda_file.close()
    print(string)
#Recibe Consulta y Evalúa
from tkinter import *
root = Tk()
root.geometry("310x180")
f1=Frame(root, height=150, width=200)
root.title('Buscador de Papers 3000')
Label1=Label(root,text='Ingrese Búsqueda:').pack()
e = Entry(root)
e.pack()

Label2=Label(root,text='Ingrese Libro:').pack()
f = Entry(root)
f.pack()
Label3=Label(root,text='Ingrese Autor:').pack()
g = Entry(root)
g.pack()

e.focus_set()


b = Button(root,text='Submit',command=printtext)
b.pack(side='bottom')
root.mainloop()

