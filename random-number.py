#computador gerar 1 numero = 73
# utilizador 1o palpite
# Tentativas +1 No caso de estar certo ou errado
# Se estiver certo, o programa acaba com uma tentativa
# Caso nao estiver certo vai continuar ate a 3a tentativa ou ate o utilizador acertar
from tkinter import *
import random


Npc = 2
nUser = 0
MaxLimit = 0 
MinLimit = 0

def acerto():
    Contador = 0
    texto = 'Teste!'
    if(Npc == nUser):
        Contador +=1
        texto="Acertaste, o numero era %d"%(Npc)
        print("Tentativas %d"%(Contador))
    else:
        Contador +=1
        print("Numero errado! tenta outra vez!")
        print("O numero esta entre: %d e %d"%(nUser,Npc+10))
        print("Tentativas %d"%(Contador))
    if(Contador == 3):
        print("O jogo acabou chegaste a 3a tentativa e nao adivinhaste!")
        exit()

window = Tk()
window.geometry('600x600')
window.title('Adivinha o numero')
window.resizable(0,0)


Button(window,text='Entrar',width='10',height='5',command=acerto).place(x=130, y=350)
Label(window,text=texto,width='10',height='5').place(x=500, y=130)
In = Entry(window,width='100').place(x=20, y=100)


while Npc != nUser:
    #converte raw_nUser (string, "palavra") para um inteiro (Numero)
    raw_nUser = input("Qual o numero:") 
    nUser = int(raw_nUser)
    #if's de forma a comparar se os numeros sao iguais ou nao









window.mainloop()

Npc=random.randint(1,100)

