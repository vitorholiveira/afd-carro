import automato

def le_arquivo():
    '''
    Função que le toda a fita de comando de um arquivo e roda ela no automato
    '''
    estado = "i0"
    nome = input("\nNome do arquivo: ")
    with open(nome, "r") as arquivo:
        linha = arquivo.readline().strip()
        linha = linha.split(',')

    for operacao in linha:
        proxEstado = automato.transicao(estado, operacao)
        if proxEstado == "indefinido":
            return estado
        estado = proxEstado
    return estado

def le_comando():
    '''
    Função que le as operações da fita de comando do terminal, uma a uma, e às roda no automato
    '''
    estado = "i0"
    while estado != "f2":
        op = input("\nDigite uma operação: ")
        proxEstado = automato.transicao(estado, op)
        if proxEstado == "indefinido":
            return estado
        estado = proxEstado
    return estado