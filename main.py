import leitura

modo = "ABABA"
while(modo != '2' and modo != '1'):
    modo = input("\nSelecione o método de leitura:\n1)Terminal \n2)Arquivo\nDigite a opcao desejada: ")

if(modo == '2'):
    estado = leitura.le_arquivo()
elif(modo == '1'):
    estado = leitura.le_comando()

if estado == "f2":
    print("\n-> COMPLETOU O PERCURSO\n")
else:
    print("\n-> OPERACCAO INDEFINIDA")
    print("-> ESTADO: " + estado + "\n")