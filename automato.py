def transicao(estado, op):
    categoria = estado[0]
    index = estado[1]

    # ciclo inicial do autômato
    if categoria == 'i':
        if index == '0' and op == 's':
            print("LIGOU O CARRO")
            return "i1"
        elif index == '1' and op == 'v':
            print("ABAIXOU O FREIO DE MAO")
            return "i2"
        elif index == '2' and op == 'm':
            print("APERTOU A EMBREGEM")
            return "m0"
        else:
            return "indefinido"
        
    # estados em que o carro está em movimento
    elif categoria == 'q':
        velocidade = int(estado[2])
        # carro para quando está na velocidade mínima ou com freada brusca
        if (estado == "q11" and op == 'f') or op == '!':
            print("PAROU O CARRO")
            return "p0"
        # não é possível acelerar quando está na velocidade máxima da marcha
        elif op == 'a' and velocidade < 2:
            print("ACELEROU O CARRO")
            return categoria + index + str(velocidade + 1)
        # não é possível frear quando o carro está na velocidade mínima da marcha
        elif op == 'f' and velocidade > 0:
            print("FREOU O CARRO")
            return categoria + index + str(velocidade - 1)
        # não é possível apertar a embreagem no ultimo estado de movimento
        elif op == 'm' and velocidade == 2 and estado != "q52":
            print("APERTOU A EMBREAGEM")
            return op + index
        # não é possível apertar a embreagem no último estado de movimento
        elif op == 'm' and velocidade == 0 and estado != "q10":
            print("APERTOU A EMBREAGEM")
            return op + str(int(index) - 1)
        elif op == 'e':
            print("GIROU 90 GRAUS PARA A ESQUERDA")
            return estado
        elif op == 'd':
            print("GIROU 90 GRAUS PARA A DIREITA")
            return estado
        else:
            return "indefinido"
        
    # estados em que o carro está no seletor de marcha (apertou a embreagem anteriormente)
    elif categoria == 'm':
        if op == index:
            print("SELEIONOU A "+index+" MARCHA")
            return 'q' + index + '2'
        elif op == str(int(index) + 1):
            print("SELECIONOU A "+str(int(index)+1)+" MARCHA")
            return 'q' + str(int(index) + 1) + '0'
        elif estado == 'm0' and op == 'n':
            print("COLOCOU EM PONTO MORTO")
            return 'f0'
        else:
            return "indefinido"
        
    # estados do ciclo final
    elif categoria == 'f':
        if index == '0' and op == '^':
            print("LEVANTOU O FREIO DE MÃO")
            return 'f1'
        elif index == '1' and op == '0':
            print("DESLIGOU O CARRO")
            return 'f2'
        else:
            return "indefinido"
        
    # estado em que o carro está parado
    # é preciso apertar a embreagem para não apagar o carro
    elif estado == "p0" and op == 'm':
        print("APERTOU A EMBREAGEM")
        return "m0"
    else:
        return "indefinido"