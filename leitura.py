import automato
from tkinter import *
from time import sleep

def le_arquivo():
    '''
    Função que def transicao(estado, operacao, labelEstado, labelSimbolo):
    op = operacao.get()
    estado = automato.transicao(estado,op)
    labelEstado.text(estado)
    labelSimbolo.text(op)lê toda a fita de comando de um arquivo e roda ela no autômato.
    Retorna o estado em que terminou a computação ou a string "indefinido" se alguma transição for indefinida.
    '''

    janela = Tk()
    janela.title("Carro")

    nome = Label(janela, text="Digite o nome de um arquivo csv:")
    nome.pack()
    entradaArq = Entry(janela, width=10)
    entradaArq.pack()

    global linha

    def abrir():
        with open(nome, "r") as arquivo:
            linha = arquivo.readline().strip()
            linha = linha.split(',')
        botao.destroy()
        nome.destroy()
        entradaArq.destroy()
        
    botao = Button(janela, text="Abrir Arquivo", command=abrir)
    botao.pack()

    global estado
    estado = "i0"

    labelOperacao = Label(janela, text="COMEÇOU O PERCURSO")
    labelOperacao.pack()
    labelEstado = Label(janela, text="Estado inicial: "+estado)
    labelEstado.pack()

    def reconhecer(linha):  
        for op in linha:
            global estado
            estado = automato.transicao(estado, op, labelOperacao, labelEstado)
            if estado == "indefinido":
                return
    
    reconhecer(linha)

    if estado == "f2":
        Label(janela, text="COMPLETOU O PERCURSO!").pack(padx=50)
    elif estado == "indefinido":
        Label(janela, text="FUNÇÃO INDEFINIDA!").pack(padx=50)
    else:
        Label(janela, text="NÃO COMPLETOU O PERCURSO!").pack(padx=50)
    
    mainloop()

    

def le_terminal():
    '''
    Função que lê as operações da fita de comando do terminal, uma a uma, e às roda no autômato
    Retorna o estado em que terminou a computação ou a string "indefinido" se alguma transição for indefinida.
    '''
    janela = Tk()
    janela.title("Carro")

    global estado
    estado = "i0"

    labelOperacao = Label(janela, text="COMEÇOU O PERCURSO")
    labelOperacao.pack()
    labelEstado = Label(janela, text="Estado inicial: "+estado)
    labelEstado.pack()
    text = Label(janela, text="Digite um símbolo:")
    text.pack(padx=100)
    operacao = Entry(janela, width=10)
    operacao.pack()

    def click():
        op = operacao.get()
        global estado
        estado = automato.transicao(estado, op, labelOperacao, labelEstado)
        operacao.delete(0, END)
        if estado == "indefinido":
            fim()

    def fim():  
        if estado == "f2":
            Label(janela, text="COMPLETOU O PERCURSO!").pack(padx=50)
        elif estado == "indefinido":
            Label(janela, text="FUNÇÃO INDEFINIDA!").pack(padx=50)
        else:
            Label(janela, text="NÃO COMPLETOU O PERCURSO!").pack(padx=50)
        text.destroy()
        operacao.destroy()
        botao.destroy()
        finaliza.destroy()

    botao = Button(janela, text="Realizar Operação", command=click)
    botao.pack()

    finaliza = Button(janela, text="Terminar Percurso", command=fim)
    finaliza.pack()

    janela.mainloop()