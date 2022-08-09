#SIMPLE CALCULATOR -- SHANMATHI MOHANRAJ

#import required libraries
import math
from tkinter import *

#create an instance
root = Tk()

#add title to the window
root.title("Simple Calculator")

#create and display input box
ent=Entry(root, width=32, font=('Arial 12'), borderwidth=3)
ent.grid(row=0, column=0, columnspan=5)

#define functions
def onclick(num):
    cur=ent.get()
    ent.delete(0, END)
    ent.insert(0, str(cur) + str(num))

def oncl():
    ent.delete(0, END)

def onadd():
    fnum=ent.get()
    global memnum
    global math
    math="add"
    memnum=eval(fnum)
    ent.delete(0, END)

def onsub():
    fnum=ent.get()
    global memnum
    global math
    math="subtract"
    memnum=eval(fnum)
    ent.delete(0, END)

def onmul():
    fnum=ent.get()
    global memnum
    global math
    math="multiply"
    memnum=eval(fnum)
    ent.delete(0, END)

def ondiv():
    fnum=ent.get()
    global memnum
    global math
    math="divide"
    memnum=eval(fnum)
    ent.delete(0, END)

def oneq():
    nnum=ent.get()
    ent.delete(0, END)

    if math=="add":
        ent.insert(0, memnum + eval(nnum))
    
    if math=="subtract":
        ent.insert(0, memnum - eval(nnum))

    if math=="multiply":
        ent.insert(0, memnum * eval(nnum))

    if math=="divide":
        ent.insert(0, memnum / eval(nnum))

def onsq():
    fnum=ent.get()
    global memnum
    memnum=str(eval(fnum))
    ent.delete(0, END)
    ent.insert(0, eval(memnum)**2)

def onsqrt():
    fnum=ent.get()
    global memnum
    memnum=str(eval(fnum))
    ent.delete(0, END)
    ent.insert(0, eval(memnum)**0.5)

#create required buttons
b1=Button(root, text="1", padx=26,pady=20, command=lambda: onclick(1), bg="#ededed", font=('Arial'))
b2=Button(root, text="2", padx=26,pady=20, command=lambda: onclick(2), bg="#ededed", font=('Arial'))
b3=Button(root, text="3", padx=26,pady=20, command=lambda: onclick(3), bg="#ededed", font=('Arial'))
b4=Button(root, text="4", padx=26,pady=20, command=lambda: onclick(4), bg="#ededed", font=('Arial'))
b5=Button(root, text="5", padx=26,pady=20, command=lambda: onclick(5), bg="#ededed", font=('Arial'))
b6=Button(root, text="6", padx=26,pady=20, command=lambda: onclick(6), bg="#ededed", font=('Arial'))
b7=Button(root, text="7", padx=26,pady=20, command=lambda: onclick(7), bg="#ededed", font=('Arial'))
b8=Button(root, text="8", padx=26,pady=20, command=lambda: onclick(8), bg="#ededed", font=('Arial'))
b9=Button(root, text="9", padx=26,pady=20, command=lambda: onclick(9), bg="#ededed", font=('Arial'))
b0=Button(root, text="0", padx=62.5,pady=20, command=lambda: onclick(0), bg="#ededed", font=('Arial'))
bdec=Button(root, text=".", padx=27.5,pady=20, command=lambda: onclick("."), bg="#ededed", font=('Arial'))
bcl=Button(root, text="C", padx=24,pady=20, command=oncl, bg="orange", font=('Arial'))
beq=Button(root, text="=", padx=28,pady=20, command=oneq, bg="orange", font=('Arial'))
bsq=Button(root, text="x\u00b2", padx=24,pady=20, command=onsq, bg="#ededed", font=('Arial'))
bsqrt=Button(root, text="\u221ax", padx=22.5,pady=20, command=onsqrt, bg="#ededed", font=('Arial'))
badd=Button(root, text="+", padx=27,pady=20, command=onadd, bg="#f7d8b0", font=('Arial'))
bsub=Button(root, text="-", padx=30,pady=20, command=onsub, bg="#f7d8b0", font=('Arial'))
bmul=Button(root, text="*", padx=29,pady=20, command=onmul, bg="#f7d8b0", font=('Arial'))
bdiv=Button(root, text="/", padx=30,pady=20, command=ondiv, bg="#f7d8b0", font=('Arial'))

#display/arrange the buttons
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=0, columnspan=2)
bdec.grid(row=5, column=2)
bcl.grid(row=1, column=0)
beq.grid(row=5, column=3)
bsq.grid(row=1, column=1)
bsqrt.grid(row=1, column=2)
badd.grid(row=4, column=3)
bsub.grid(row=3, column=3)
bmul.grid(row=2, column=3)
bdiv.grid(row=1, column=3)

#run the window
root.mainloop()