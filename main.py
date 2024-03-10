import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import DoubleVar

from PIL import ImageTk, Image

window= tk.Tk()
window.title("Siemens LOGO! Offset/Gain calculator")
window.geometry('1000x500')

LabelLowValueI = Label(window,text='Input Low Value:',fg='blue',font=('Arial',14))
LabelLowValueI.grid(row=0,column=0,padx=20,pady=5,sticky='W')

LabelHighValueI = Label(window,text='Input High Value:',fg='blue',font=('Arial',14))
LabelHighValueI.grid(row=1,column=0,padx=20,pady=5,sticky='W')

LabelLowValueO = Label(window,text='Output Value by Low Value of Input:',fg='blue',font=('Arial',14))
LabelLowValueO.grid(row=2,column=0,padx=20,pady=5)

LabelHighValueO = Label(window,text='Output Value by High Value of Input:',fg='blue',font=('Arial',14))
LabelHighValueO.grid(row=3,column=0,padx=20,pady=5)


XA=DoubleVar()
XB=DoubleVar()
YA=DoubleVar()
YB=DoubleVar()


textboxXA = Entry(window,textvariable=XA,fg='black',font=('Arial',14))
textboxXA.grid(row=0,column=1)

textboxXB = Entry(window,textvariable=XB,fg='black',font=('Arial',14))
textboxXB.grid(row=1,column=1)

textboxYA = Entry(window,textvariable=YA,fg='black',font=('Arial',14))
textboxYA.grid(row=2,column=1)

textboxYA = Entry(window,textvariable=YB,fg='black',font=('Arial',14))
textboxYA.grid(row=3,column=1)


def Calculate():
    Var1=XA.get()
    Var2=XB.get()
    Var3=YA.get()
    Var4=YB.get()

    Gain=float((Var4-Var3)/(Var2-Var1))
    Offset=float(Var3-(Var1*Gain))

    Gain=round(Gain,4)
    Offset=round(Offset,0)

    Gainbox.insert(0,str(Gain))
    OffsetBox.insert(0,str(Offset))

    
ButtonCalc = Button(window,text='Calculate',command=Calculate,fg='blue',font=('Arial',14))
ButtonCalc.grid(row=4,column=1,padx=20,pady=5)

Gainbox = Entry(window,fg='blue',font=('Arial',14))
Gainbox.grid(row=5,column=1,padx=20,pady=5)

OffsetBox = Entry(window,fg='blue',font=('Arial',14))
OffsetBox.grid(row=6,column=1,padx=20,pady=5)

GainLabel = Label(window,text="Gain",fg='blue',font=('Arial',14))
GainLabel.grid(row=5, column=0,padx=20,pady=5,sticky='E')

OffsetLabel = Label(window,text="Offset",fg='blue',font=('Arial',14))
OffsetLabel.grid(row=6,column=0,padx=20,pady=5,sticky='E')

window.mainloop()