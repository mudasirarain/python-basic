import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('400x300')
window.title("my calculator")

#logic
def showNum(x):
    calc= screen_var.get()
    calc = calc + str(x)
    screen_var.set(calc)

def btnCencelfunc():
    screen_var.set(0)

def equalfunction():    
    calc = screen_var.get()
    ans = eval(calc)
    screen_var.set(ans)
    
#interface
screen_var = tk.StringVar()
screen = ttk.Entry(window,font="arial 14",textvariable=screen_var)
screen.pack(side="top",fill="x",pady=10)

btnPanel= ttk.Frame(window )
btnPanel.pack()

#num0 = ttk.Button(btnPanel,text="0")
#num1 = ttk.Button(btnPanel,text="1")
#num2 = ttk.Button(btnPanel,text="2")
#num3 = ttk.Button(btnPanel,text="3")
#num4 = ttk.Button(btnPanel,text="4")
#num5 = ttk.Button(btnPanel,text="5")
#num6 = ttk.Button(btnPanel,text="6")
#num7 = ttk.Button(btnPanel,text="7")
#num8 = ttk.Button(btnPanel,text="8")
#num9 = ttk.Button(btnPanel,text="9")

#num0.grid(row=0,column=0)
#num1.grid(row=0,column=1)
#num2.grid(row=0,column=2)
#num3.grid(row=0,column=3)
#num4.grid(row=1,column=0)
#num5.grid(row=1,column=1)
#num6.grid(row=1,column=2)
#num7.grid(row=1,column=3)
#num8.grid(row=2,column=0)
#num9.grid(row=2,column=1)


btnNums = []
x = 0
for i in range(0,3):
    for j in range(0,3):
        x=x+1
        btnNums = ttk.Button(btnPanel,text=x,command=lambda val=x: showNum(val)).grid(row=i,column=j)


btnDivide = ttk.Button(btnPanel,text="/",command=lambda val=x:showNum("/")).grid(row=0,column=3)
btnMultiply = ttk.Button(btnPanel,text="*",command=lambda val=x:showNum("*")).grid(row=1,column=3)
btnMinus = ttk.Button(btnPanel,text="-",command=lambda val=x:showNum("-")).grid(row=2,column=3)
btnPlus = ttk.Button(btnPanel,text="+",command=lambda val=x:showNum("+")).grid(row=3,column=3)
btnNum0 = ttk.Button(btnPanel,text="0",command=lambda val=x:showNum("0")).grid(row=3,column=0)
btncencle = ttk.Button(btnPanel,text="c",command=btnCencelfunc).grid(row=3,column=1)
btnequal = ttk.Button(btnPanel,text="=",command=equalfunction).grid(row=3,column=2)

#run
window.mainloop()
