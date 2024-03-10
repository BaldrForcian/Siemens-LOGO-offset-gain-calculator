import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import DoubleVar

from PIL import ImageTk, Image



#initlialization of window
window= tk.Tk()
window.title("Siemens LOGO! Offset/Gain calculator")
window.geometry('900x500')

imageMATH = Image.open('siemens_logo_icon_170741.png')
ico = ImageTk.PhotoImage(imageMATH)
window.wm_iconphoto(False,ico)

#creates the onescreen text
LabelLowValueI = Label(window,text='Input Low Value(0.00-10.00V):',fg='blue',font=('Arial',14))
LabelLowValueI.grid(row=0,column=0,padx=20,pady=5,sticky='W')

LabelHighValueI = Label(window,text='Input High Value(0.00-10.00V):',fg='blue',font=('Arial',14))
LabelHighValueI.grid(row=1,column=0,padx=20,pady=5,sticky='W')

LabelLowValueO = Label(window,text='Output Value by Low Value of Input:',fg='blue',font=('Arial',14))
LabelLowValueO.grid(row=2,column=0,padx=20,pady=5)

LabelHighValueO = Label(window,text='Output Value by High Value of Input:',fg='blue',font=('Arial',14))
LabelHighValueO.grid(row=3,column=0,padx=20,pady=5)

#input variables
XA=DoubleVar()
XB=DoubleVar()
YA=DoubleVar()
YB=DoubleVar()


#crates the input textboxes
textboxXA = Entry(window,width=10,textvariable=XA,fg='black',font=('Arial',14))
textboxXA.grid(row=0,column=1,sticky='W')

textboxXB = Entry(window,width=10,textvariable=XB,fg='black',font=('Arial',14))
textboxXB.grid(row=1,column=1,sticky='W')

textboxYA = Entry(window,width=10,textvariable=YA,fg='black',font=('Arial',14))
textboxYA.grid(row=2,column=1,sticky='W')

textboxYA = Entry(window,width=10,textvariable=YB,fg='black',font=('Arial',14))
textboxYA.grid(row=3,column=1,sticky='W')

#calculates the gain and offset, writes it to the approprate boxes
def Calculate():
    
    Gainbox.delete(0,'end')
    OffsetBox.delete(0,'end')
    V1Textbox.delete(0,'end')
    V2Textbox.delete(0,'end')
    V3Textbox.delete(0,'end')
    V4Textbox.delete(0,'end')

    
    Var1=XA.get()
    Var2=XB.get()
    Var3=YA.get()
    Var4=YB.get()

    Var1=Var1*100
    Var2=Var2*100

    Gain=float((Var4-Var3)/(Var2-Var1))
    Offset=float(Var3-(Var1*Gain))

    Gain=round(Gain,4)
    Offset=round(Offset,0)

    V2=float(Gain*10000)
    V3=float(10000)
    V4=float(Offset)

    Gainbox.insert(0,str(Gain))
    OffsetBox.insert(0,str(Offset))
    V1Textbox.insert(0,"input from analog amp")
    V2Textbox.insert(0,str(V2))
    V3Textbox.insert(0,str(V3))
    V4Textbox.insert(0,str(V4))


#creates the button for calculate
ButtonCalc = Button(window,text='Calculate',command=Calculate,fg='blue',font=('Arial',14))
ButtonCalc.grid(row=4,column=1,padx=20,pady=5)

#creates the textboxes for gain and offset
Gainbox = Entry(window,width=20,fg='blue',font=('Arial',14))
Gainbox.grid(row=5,column=1,padx=20,pady=5,sticky='E')

OffsetBox = Entry(window,width=20,fg='blue',font=('Arial',14))
OffsetBox.grid(row=6,column=1,padx=20,pady=5,sticky='E')

#creates the onescreen text for gain and offfset
GainLabel = Label(window,width=20,text="Gain",fg='blue',font=('Arial',14))
GainLabel.grid(row=5, column=0,padx=20,pady=5,sticky='E')

OffsetLabel = Label(window,width=20,text="Offset",fg='blue',font=('Arial',14))
OffsetLabel.grid(row=6,column=0,padx=20,pady=5,sticky='E')

#creates onescreen text for Mathematical instruction inputs
V1Label = Label(window,text="V1", fg='blue',font=('Arial',14))
V1Label.grid(row=0, column=2,sticky='E')

V2Label = Label(window,text="V2", fg='blue',font=('Arial',14))
V2Label.grid(row=1, column=2,sticky='E')

V3Label = Label(window,text="V3", fg='blue',font=('Arial',14))
V3Label.grid(row=2, column=2,sticky='E')

V4Label = Label(window,text="V4", fg='blue',font=('Arial',14))
V4Label.grid(row=3, column=2,sticky='E')

#creates textboxes for mathematical instruction inputs
V1Textbox = Entry(window,width= 20,fg='blue',font=('Airal',14) )
V1Textbox.grid(row=0,column=3)

V2Textbox = Entry(window,width= 10,fg='blue',font=('Airal',14) )
V2Textbox.grid(row=1,column=3,sticky='W')

V3Textbox = Entry(window,width= 10,fg='blue',font=('Airal',14) )
V3Textbox.grid(row=2,column=3,sticky='W')

V4Textbox = Entry(window,width= 10,fg='blue',font=('Airal',14) )
V4Textbox.grid(row=3,column=3,sticky='W')


window.mainloop()