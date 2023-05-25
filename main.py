from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.config(padx= 2, pady= 2 , background='#AAA')
janela.resizable(False, False)
etiqueta = Label(janela , text="Ainda não possue nenhuma conta", justify=CENTER,
font=('fontana', 16 , 'bold'), bg='#AAA') 

entrada = Entry(janela, width=15 , borderwidth=6, relief=SOLID, bg='#FFFFFF', fg='#000',
font=('futura',25, "bold"), justify=CENTER )
# etiqueta.grid(
#     row=0,
#     column=4)
entrada.grid(
    row=0,
    column=0,
    columnspan=3,
    pady= 2
)
#funções 
def click_btn():
    return 


# botões 
divide = Button(janela,
                text="÷" , font=('fontana' , 12 , 'bold'),padx=20 , pady= 20,
                bg='#FFDB58', fg="#000000" , relief= FLAT, activebackground='#FFA500')

divide.grid(row= 0 , column=3 ,padx=0 , pady= 5  )

um = Button(janela , 
                text='1', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(1))

um.grid(
     row=1 , 
     column=0 , 
     padx= 0  , 
     pady= 5)


dois = Button(janela , 
                text='2', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(2))

dois.grid(
     row=1 , 
     column=1 , 
     padx= 0  , 
     pady= 5)

tres = Button(janela , 
                text='3', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(3))

tres.grid(
     row=1 , 
     column=2 , 
     padx= 0  , 
     pady= 5)

quatro = Button(janela , 
                text='4', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(4))

quatro.grid(
     row=2 , 
     column=0 , 
     padx= 0  , 
     pady= 5)

cinco = Button(janela , 
                text='5', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(5))

cinco.grid(
     row=2 , 
     column=1 , 
     padx= 0  , 
     pady= 5)

seis = Button(janela , 
                text='6', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(6))

seis.grid(
     row=2 , 
     column=2 , 
     padx= 0  , 
     pady= 5)

sete = Button(janela , 
                text='7', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(7))

sete.grid(
     row=3 , 
     column=0 , 
     padx= 0  , 
     pady= 5)

oito = Button(janela , 
                text='8', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(8))

oito.grid(
     row=3 , 
     column=1 , 
     padx= 0  , 
     pady= 5)

nove = Button(janela , 
                text='9', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 20 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(9))

nove.grid(
     row=3 , 
     column=2 , 
     padx= 0  , 
     pady= 5)

zero = Button(janela , 
                text='0', 
                font=( 'fontana' , 12 , 'bold') , 
                padx= 68 , pady= 20 ,
                bg='#FFDB58', fg="#000000" , 
                relief= FLAT, 
                activebackground='#FFA500', 
                command=lambda: click_btn(0))

zero.grid(
     row=4 , 
     column=0, 
     padx= 0  , 
     pady= 5,
     columnspan= 2)

janela.mainloop()