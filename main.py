from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.config(padx= 2, pady= 2 , background='#AAA')
janela.resizable(False, False)
primeiro_numero = 0
operacao = ""


entrada = Entry(janela, 
               width=15 , 
               borderwidth=6, 
               relief=SOLID, 
               bg='#FFFFFF', 
               fg='#000',
               font=('futura',30, "bold"), 
               justify=CENTER,) 

entrada.grid(
    row=0,
    column=0,
    columnspan=3,
    pady= 6,
    padx= 10
)
#funções 

def calcula_raiz_quadrada():
     numero = float(entrada.get())
     resultado =numero ** 0.5
     entrada.delete(0,END)
     entrada.insert(0, str(f'{resultado:.2f}'))




def click_btn(numero):

     numero = int(numero)
     entrada.insert(END ,numero)
 

def definir_operacao(op):
     global primeiro_numero
     global operacao
     operacao = op
     primeiro_numero = float(entrada.get())
     entrada.delete( 0 , END)

def tecla_precionada(event):
     tecla = event.char
     if tecla.isdigit():
          click_btn(int(tecla))


def calcular():

     global primeiro_numero
     segundo_numero = float(entrada.get())

     if operacao == "*" :
          resultado = primeiro_numero * segundo_numero
          
     if operacao ==  '/':
          resultado = primeiro_numero / segundo_numero

     if operacao == '+':
          resultado = primeiro_numero + segundo_numero

     if operacao  == '-':
          resultado = primeiro_numero - segundo_numero

     if operacao == '**':
          resultado = primeiro_numero ** segundo_numero

     if operacao == '%':
          resultado = (primeiro_numero / segundo_numero  ) * 100

     entrada.delete(0 , END)
     entrada.insert(0 , str(f'{resultado:.2f}'))
     primeiro_numero = 0

def add_ponto():
     valorAtual = entrada.get()
     if '.' not in valorAtual:
          entrada.insert(END,'.')


def apaga():
     entrada.delete(0 , END)


def cria_btn(aparece,texto,espacox,espacoy,fundo,cor_fonte,cor_click,comando,style):
     """
     aparece = onde ou em qual "janela" o resultado ira aparecer;
     texto = o texto que ira aparecer no botão;
     espacox = o pad em relação ao eixo X;
     espacoy = o pad em relação ao eixo Y;
     fundo = a cor de fundo do seu botão;
     cor_fonte = a cor da fonte;
     cor_click = a cor do botão quando houver o click;
     comando = o comando ou a função que voçê quiser atribuir ;
     style = o estilo da borda do botão;
     """
     botao = Button(aparece,
                    text=texto,
                    font=('fontana', 12 , 'bold'),
                    padx=espacox ,
                    pady=espacoy ,
                    bg= fundo, 
                    fg= cor_fonte,
                    activebackground= cor_click,
                    command= comando,
                    relief= style)
     
     return botao

def cria_grid(variavel,coluna,linha , espacox=0,espacoy=5, espaco=1):
     '''
     variavel = o nome da variavel do botão descrito acima;
     coluna = em qual coluna sera posicionado o botão;
     linha = em qual linha sera posicionado o botão;
     espacox = o pad em relação ao eixo X;
     espacoy = o pad em relação ao eixo Y;
     espaco = o tanto de linhas que haverá em relação aos outros botões;
     '''
     variavel.grid(row= coluna,column= linha , padx= espacox , pady= espacoy ,columnspan= espaco)

janela.bind('<Key>', tecla_precionada)
um = cria_btn(janela,"1",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(1), FLAT)
cria_grid(um,1 ,0,0,5)

dois = cria_btn(janela,"2",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(2), FLAT)
cria_grid(dois,1 ,1,0,5)

tres = cria_btn(janela,"3",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(3), FLAT)
cria_grid(tres,1 ,2,0,5)

quatro = cria_btn(janela,"4",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(4), FLAT)
cria_grid(quatro,2 ,0,0,5)

cinco = cria_btn(janela,"5",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(5), FLAT)
cria_grid(cinco,2 ,1,0,5)

seis = cria_btn(janela,"6",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(6), FLAT)
cria_grid(seis,2 ,2,0,5)

sete = cria_btn(janela,"7",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(7), FLAT)
cria_grid(sete,3 ,0,0,5)

oito = cria_btn(janela,"8",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(8), FLAT)
cria_grid(oito,3 ,1,0,5)

nove = cria_btn(janela,"9",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(9), FLAT)
cria_grid(nove,3 ,2,0,5)

zero = cria_btn(janela,"0",90 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:click_btn(0), FLAT)
cria_grid(zero,4 ,0,0,5, 2)

apagar = cria_btn(janela,"C",30 , 20 ,'#FFDB58',"#000000",'#FFA500',lambda:apaga(), FLAT)
cria_grid(apagar,0 ,4,0,5,2)

mais = cria_btn(janela,"+",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:definir_operacao('+'), FLAT)
cria_grid(mais,1 ,3,0,5,2)

menos = cria_btn(janela,"-",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:definir_operacao('-'), FLAT)
cria_grid(menos,2 ,3,0,5,2)

divide = cria_btn(janela,"÷",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:definir_operacao('/'), FLAT)
cria_grid(divide,3 ,3,0,5,2)

vezes = cria_btn(janela,"X",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:definir_operacao('*'), FLAT)
cria_grid(vezes,4 ,2,0,5,2)

igual = cria_btn(janela,"=",30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda:calcular(), FLAT)
cria_grid(igual,4 ,3,0,5 ,2 )

potencia = cria_btn(janela , '^' , 30 , 30 ,'#FFDB58',"#000000",'#FFA500' , lambda: definir_operacao('**'), FLAT)
cria_grid(potencia, 5 , 0 , 0 , 5, )

raiz_quadrada = cria_btn(janela,'√', 30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda: calcula_raiz_quadrada(), FLAT)
cria_grid(raiz_quadrada,5 , 1 , 0 ,5,)

porcentagem = cria_btn(janela,'%', 30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda: definir_operacao('%'), FLAT)
cria_grid(porcentagem,5 , 2 , 0 ,5,2)

ponto = cria_btn(janela,'.', 30 , 30 ,'#FFDB58',"#000000",'#FFA500',lambda: add_ponto(), FLAT)
cria_grid(ponto,5 , 3 , 0 ,5,2)
janela.mainloop()