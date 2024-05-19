#importar as bibliotecas
from tkinter import *
from tkinter import messagebox

#Criar nossa janela

Janela = Tk()
Janela.title("Castel's Barbearia - Painel de acesso")
Janela.geometry("600x300")
Janela.configure(background="white")
#Faz com que a janela não possa mudar sua propriedade
#Não tem necessidade de ser responsivo
Janela.resizable(width=False, height=False)

#============== Carregando Imagens =============
logo = PhotoImage("icons/castelo.png")



#============== Widgests ===============
LeftFrame = Frame(Janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(Janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTCLUB")
LogoLabel.place(x=50, y=100)


Janela.mainloop()
