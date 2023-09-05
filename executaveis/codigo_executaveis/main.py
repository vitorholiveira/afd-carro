#!/usr/bin/python3

from tkinter import *
import leitura

janela = Tk()
janela.title("ababa")
janela.geometry("300x300")

label = Label(janela, text="Selecione o método de interação:")
label.pack()

def fimMenu(leitura):
    '''
    Função que apaga os itens do Menu.
    Tem como parâmetro uma função referente ao modo de interação com o usuário.
    '''
    label.destroy()
    botaoInput.destroy()
    botaoArquivo.destroy()
    leitura(janela)

botaoInput = Button(janela, text="Input", command= lambda : fimMenu(leitura.le_input))
botaoInput.pack()

botaoArquivo = Button(janela, text="Arquivo", command= lambda : fimMenu(leitura.le_arquivo))
botaoArquivo.pack()

janela.mainloop()
