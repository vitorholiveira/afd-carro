from tkinter import *
import leitura

menu = Tk()
menu.title("ababa")

Label(menu, text="Selecione o método de interação:").pack(padx=15)

Button(menu, text="Manual", command=leitura.le_terminal).pack()

Button(menu, text="Automático", command=leitura.le_arquivo).pack()

menu.mainloop()