import automato
from tkinter import *

def le_arquivo(janela):
    '''
    Função que pede para o usuário o nome de um arquivo csv e roda no autômato.
    Pode fazer passo a passo ou realizar o reconhecimento direto.
    '''
    nome = Label(janela, text="Digite o nome de um arquivo csv:")
    entradaArq = Entry(janela, width=30)
    nome.pack()
    entradaArq.pack()

    # Abre o arquivo
    def abrir():
        global linha
        with open(entradaArq.get(), "r") as arquivo:
            linha = arquivo.readline().strip()
            linha = linha.split(',')
        botaoAbrir.destroy()
        nome.destroy()
        entradaArq.destroy()

        # Mostra a operação realizada e a função de transição
        labelOperacao = Label(janela, text="COMEÇOU O PERCURSO")
        labelEstado = Label(janela, text="Estado inicial: i0")
        labelOperacao.pack()
        labelEstado.pack()

        global estado
        estado = "i0"

        # Reconhece um simbolo por vez
        def passo():
            global estado
            estado = automato.transicao(estado, linha[0], labelOperacao, labelEstado)
            linha.pop(0)
            if estado == "indefinido" or len(linha) == 0:
                fimArquivo()

        # Reconhece toda palavra do arquivo
        def reconhecer():
            global estado
            for op in linha:
                estado = automato.transicao(estado, op, labelOperacao, labelEstado)
                if estado == "indefinido":
                    break
            fimArquivo()

        # Apaga os itens da tela atual e chama a função que gera a tela final
        def fimArquivo():
            botaoPasso.destroy()
            botaoReconhecer.destroy()
            fim(janela, estado)

        botaoPasso = Button(janela, text="Próxima operação", command=passo)
        botaoReconhecer = Button(janela, text="Reconhecer", command=reconhecer)
        botaoPasso.pack()
        botaoReconhecer.pack()
        
    botaoAbrir = Button(janela, text="Abrir Arquivo", command=abrir)
    botaoAbrir.pack()

# ------------------------------------------------------------------------------------

def le_input(janela):
    '''
    Função que pede para o usuário símbolos e roda no autômato, um por vez.
    '''
    # Interface de interação com o usuário
    # Mostra a operação realizada e a função de transição
    labelOperacao = Label(janela, text="COMEÇOU O PERCURSO")
    labelEstado = Label(janela, text="Estado inicial: i0")
    labelTexto = Label(janela, text="Digite um símbolo:")
    entryOperacao = Entry(janela, width=10)
    labelOperacao.pack()
    labelEstado.pack()
    labelTexto.pack()
    entryOperacao.pack()

    global estado
    estado = "i0"

    # Reconhece um input do usuário
    def click():
        op = entryOperacao.get()
        global estado
        estado = automato.transicao(estado, op, labelOperacao, labelEstado)
        entryOperacao.delete(0, END)
        if estado == "indefinido":
            fimInput()

    # Apaga os itens da tela atual e chama a função que gera a tela final
    def fimInput():
        labelTexto.destroy()
        entryOperacao.destroy()
        botao.destroy()
        botaoFim.destroy()
        fim(janela, estado)

    botao = Button(janela, text="Realizar Operação", command=click)
    botaoFim = Button(janela, text="Terminar Percurso", command=fimInput)
    botao.pack()
    botaoFim.pack()

# ------------------------------------------------------------------------------------

def fim(janela, estado):
    '''
    Função para gerar a tela final, após uma palavra ser reconhecida
    '''

    if estado == "f2":
        Label(janela, text="COMPLETOU O PERCURSO!").pack()
    elif estado == "indefinido":
        Label(janela, text="FUNÇÃO INDEFINIDA!").pack()
    else:
        Label(janela, text="NÃO COMPLETOU O PERCURSO!").pack()
