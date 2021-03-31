from tkinter import *

soma= 3
num1 = 0
num2 = 0

window = Tk()
window.title('Calculator')
window.geometry('400x600')
window.configure(bg='#4d989e')


Button(window,text='CE',padx = 2,width='10',height='5').place(x=246 ,y = 200)
Button(window,text='/',padx = 2,width='10',height='5').place(x=246 ,y = 300)
Button(window,text='x',padx = 2,width='10',height='5').place(x=246 ,y = 400)
Button(window,text='=',padx = 2,width='10',height='5').place(x=246 ,y = 500)
Button(window,text='+',padx = 2,width='10',height='5').place(x=164 ,y = 500)
Button(window,text='0',padx = 2,width='10',height='5').place(x=82 ,y = 500)
Button(window,text='-',padx = 2,width='10',height='5').place(x=0 ,y = 500)
Button(window,text='9',padx = 2,width='10',height='5',num1='9').place(x=164 ,y = 400)
Button(window,text='8',padx = 2,width='10',height='5',num1='8').place(x=82 ,y = 400)
Button(window,text='7',padx = 2,width='10',height='5',num1='7').place(x=0 ,y = 400)
Button(window,text='6',padx = 2,width='10',height='5',num1='6').place(x=164 ,y = 300)
Button(window,text='5',padx = 2,width='10',height='5',num1='5').place(x=82 ,y = 300)
Button(window,text='4',padx = 2,width='10',height='5',num1='4').place(x=0 ,y = 300)
Button(window,text='3',padx = 2,width='10',height='5',num1='3').place(x=164 ,y = 200)
Button(window,text='2',padx = 2,width='10',height='5',num1='2').place(x=82 ,y = 200)
Button(window,text='1',padx = 2,width='10',height='5',num1='1').place(x=0 ,y = 200)


Label(window,text=num1,padx = 2,width='46',height='5').place(x=0 ,y = 100)


window.mainloop()