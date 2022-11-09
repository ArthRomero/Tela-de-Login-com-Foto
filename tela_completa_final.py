
import requests
from tkinter import *
import Tirar_Foto

def autenticar():
    bd_usuario = "Arthur"
    bd_senha = "4321"
    d_usuario = (usuario.get())
    d_senha = (senha.get())
    if ((bd_usuario == d_usuario)and(bd_senha == d_senha)):
        certo = Tk()
        certo.geometry("300x100")
        certo.title("Login Correto")
        texto = Label(certo, text = "Login Correto")

        certo.columnconfigure(0, weight = 1)
        certo.columnconfigure(1, weight = 2)
        certo.rowconfigure(0, weight = 0)
        certo.rowconfigure(1, weight = 1)

        texto.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

    if ((bd_usuario != d_usuario)or(bd_senha != d_senha)):
        Tirar_Foto.foto()
        errado = Tk()
        errado.geometry("300x100")
        errado.title("Login Incorreto")
        texto = Label(errado, text = "Login Incorreto")

        errado.columnconfigure(0, weight = 1)
        errado.columnconfigure(1, weight = 2)
        errado.rowconfigure(0, weight = 0)
        errado.rowconfigure(1, weight = 1)

        texto.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

janela = Tk()
janela.geometry("220x100")
janela.title('Acesso')
janela.resizable(0, 0)

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=2)

usuario = StringVar()  
senha = StringVar() 

usuario_label = Label(janela, text="Usuário:")
usuario_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
usuario_entry = Entry(janela,textvariable=usuario)
usuario_entry.grid(column=1, row=0, sticky=EW, padx=5,pady=5)

senha_label = Label(janela, text="Senha:")
senha_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
senha_entry = Entry(janela, textvariable=senha, show="*")
senha_entry.grid(column=1, row=1, sticky=EW, padx=5,pady=5)

botao1 = Button(janela, text="Autenticar", command=autenticar)
botao1.grid(column=1, row=3, sticky=E, padx=5, pady=5)

janela.mainloop()
