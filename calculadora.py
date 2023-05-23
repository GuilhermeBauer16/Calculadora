import requests
from tkinter import *

janela = Tk()
janela.mainloop()
def titulo(string):
    print("=/" * 30)
    print(string.center(60))
    print('=/' * 30)


def verifica_int(valor):

    while True:
        numero = input(valor)

        try:
            int_numero = int(numero)
            break
        except ValueError:
            print('Por favor digite um numero!')

    return int_numero


def verifica_float(valor):

    while True:

        numero = input(valor)

        try:
            float_numero = float(numero)
            break

        except ValueError:
            print("Por favor informe um numero!")
        
    return float_numero


titulo('Calculadora')  
print("""escolha uma opção
[0] sair
[1] adição 
[2] subtração
[3] divisao
[4] multipicação
""")

while True:

    numero1 = verifica_float("Imforme o primeiro número: ")
    numero2 = verifica_float("Imformeo segundo número: ")
    opcao = verifica_int("imforme sua opção: ")
