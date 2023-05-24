import tkinter as tk

def janela():
    janela = tk.Tk()
    janela.title("Calculadora")
    janela.config(padx= 10 , pady= 10 , background='#aaa')
    janela.resizable(False, False)
    return janela


def label(janela):
    label = tk.label(
    janela ,text='Ainda não possue nenhuma conta',
    anchor='e' , justify='right' , background='#fff')
    return label