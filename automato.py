from PIL import ImageTk,Image

def transicao(estado, op, labelOperacao, labelEstado, img):
    '''
    Função de transição autômato.
    Retorna o próximo estado se a função de transição for definida, caso contrário retorna a string "indefinido".
    '''
    categoria = estado[0]
    index = estado[1]
    operacao = "?"

    # ciclo inicial do autômato
    if categoria == 'i':
        if index == '0' and op == 's':
            operacao = "LIGOU O CARRO" 
            proxEstado = "i1"
            imagem = ImageTk.PhotoImage(Image.open("imagens/ligarcarro.png"))
        elif index == '1' and op == 'v':
            operacao = "ABAIXOU O FREIO DE MÃO"
            proxEstado = "i2"
            imagem = ImageTk.PhotoImage(Image.open("imagens/freio_de_mao.png"))
        elif index == '2' and op == 'm':
            operacao = "APERTOU A EMBREGEM"
            proxEstado = "m0"
            imagem = ImageTk.PhotoImage(Image.open("imagens/embreagem.png"))
        else:
            proxEstado = "indefinido"
        
    # estados em que o carro está com a marcha engatada
    elif categoria == 'q':
        velocidade = int(estado[2])
        # carro para quando está na velocidade mínima ou com freada brusca
        if (estado == "q11" and op == 'f') or op == '!':
            operacao = "PAROU O CARRO"
            proxEstado = "p0"
            imagem = ImageTk.PhotoImage(Image.open("imagens/carroparado.png"))
        # não é possível acelerar quando está na velocidade máxima da marcha
        elif op == 'a' and velocidade < 2:
            operacao = "ACELEROU O CARRO"
            proxEstado = 'q' + index + str(velocidade + 1)
            imagem = ImageTk.PhotoImage(Image.open("imagens/acelerar.png"))
        # não é possível frear quando o carro está na velocidade mínima da marcha
        elif op == 'f' and velocidade > 0:
            operacao = "FREOU O CARRO"
            proxEstado = 'q' + index + str(velocidade - 1)
            imagem = ImageTk.PhotoImage(Image.open("imagens/frear.png"))
        # não é possível apertar a embreagem no ultimo estado de movimento
        elif op == 'm' and velocidade == 2 and estado != "q52":
            operacao = "APERTOU A EMBREAGEM"
            proxEstado = 'm' + index
            imagem = ImageTk.PhotoImage(Image.open("imagens/embreagem.png"))
        # não é possível apertar a embreagem no primeiro estado de movimento
        elif op == 'm' and velocidade == 0 and estado != "q10":
            operacao = "APERTOU A EMBREAGEM"
            proxEstado = 'm' + str(int(index) - 1)
            imagem = ImageTk.PhotoImage(Image.open("imagens/embreagem.png"))
        elif op == 'e':
            operacao = "DOBROU PARA A ESQUERDA"
            proxEstado = estado
            imagem = ImageTk.PhotoImage(Image.open("imagens/dobrar.png"))
        elif op == 'd':
            operacao = "DOBROU PARA A DIREITA"
            proxEstado = estado
            imagem = ImageTk.PhotoImage(Image.open("imagens/dobrar.png"))
        else:
            proxEstado = "indefinido"
        
    # estados em que o carro está no seletor de marcha (apertou a embreagem anteriormente)
    elif categoria == 'm':
        if op == index and index != '0':
            operacao = "SELEIONOU A "+index+"ª MARCHA"
            proxEstado = 'q' + index + '2'
            imagem = ImageTk.PhotoImage(Image.open("imagens/marcha.png"))
        elif op == str(int(index) + 1):
            operacao = "SELECIONOU A "+str(int(index)+1)+"ª MARCHA"
            proxEstado = 'q' + str(int(index) + 1) + '0'
            imagem = ImageTk.PhotoImage(Image.open("imagens/marcha.png"))
        elif index == '0' and op == 'n':
            operacao = "COLOCOU EM PONTO MORTO"
            proxEstado = "f0"
            imagem = ImageTk.PhotoImage(Image.open("imagens/marcha.png"))
        else:
            proxEstado = "indefinido"
        
    # estados do ciclo final
    elif categoria == 'f':
        if index == '0' and op == '^':
            operacao = "LEVANTOU O FREIO DE MÃO"
            proxEstado = "f1"
            imagem = ImageTk.PhotoImage(Image.open("imagens/freio_de_mao.png"))
        elif index == '1' and op == '0':
            operacao = "DESLIGOU O CARRO"
            proxEstado = "f2"
            imagem = ImageTk.PhotoImage(Image.open("imagens/ligarcarro.png"))
        else:
            proxEstado = "indefinido"
        
    # estado em que o carro está parado
    elif estado == "p0" and op == 'm':
        operacao = "APERTOU A EMBREAGEM"
        proxEstado = "m0"
        imagem = ImageTk.PhotoImage(Image.open("imagens/embreagem.png"))
    else:
        proxEstado = "indefinido"

    if proxEstado != "indefinido":
        img.configure(image=imagem)
        img.image = imagem
    
    labelOperacao.config(text=operacao)
    labelEstado.config(text="("+estado+","+op+") -> "+proxEstado)
    return proxEstado