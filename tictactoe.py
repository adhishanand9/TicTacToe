import tkinter as tt
from tkinter import messagebox

tic=tt.Tk()
tic.title="tictac"
tic.geometry('197x355')
flag=True
def methods(buttons):
    global flag
    if buttons["text"]=="     " and flag==True:
        buttons["text"]="X"
        flag=False
        xgt=chck()
    elif buttons["text"]=="     " and flag==False:
        buttons["text"]="O"
        flag=True
        xgr=chck()
def chck():
    if((button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X") or
        (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X") or
        (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X") or
        (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X") or
        (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X") or
        (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X") or
        (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X") or
        (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X")):
        tt.messagebox.showinfo("Result","Winner is X")
    elif((button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O") or
        (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O") or
        (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O") or
        (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O") or
        (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O") or
        (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O") or
        (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O") or
        (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O")):
        tt.messagebox.showinfo("Result","Winner is O")
def reset():
   button1["text"]="     "
   button2["text"]="     "
   button3["text"]="     "
   button4["text"]="     "
   button5["text"]="     "
   button6["text"]="     "
   button7["text"]="     "
   button8["text"]="     "
   button9["text"]="     "
button1=tt.Button(tic,text="     ",command=lambda:methods(button1),width=8,height=4)
button1.grid(column=0,row=0)
button2=tt.Button(tic,text="     ",command=lambda:methods(button2),width=8,height=4)
button2.grid(column=1,row=0)
button3=tt.Button(tic,text="     ",command=lambda:methods(button3),width=8,height=4)
button3.grid(column=2,row=0)
button4=tt.Button(tic,text="     ",command=lambda:methods(button4),width=8,height=4)
button4.grid(column=0,row=1)
button5=tt.Button(tic,text="     ",command=lambda:methods(button5),width=8,height=4)
button5.grid(column=1,row=1)
button6=tt.Button(tic,text="     ",command=lambda:methods(button6),width=8,height=4)
button6.grid(column=2,row=1)
button7=tt.Button(tic,text="     ",command=lambda:methods(button7),width=8,height=4)
button7.grid(column=0,row=2)
button8=tt.Button(tic,text="     ",command=lambda:methods(button8),width=8,height=4)
button8.grid(column=1,row=2)
button9=tt.Button(tic,text="     ",command=lambda:methods(button9),width=8,height=4)
button9.grid(column=2,row=2)
button10=tt.Button(tic,text= "   Reset   ",command=lambda:reset(),width=8,height=4)
button10.grid(row=4,column=0,columnspan=3,sticky=tt.E+tt.W)
button11=tt.Button(tic,text= "   Exit   ",command=lambda:tic.destroy(),width=8,height=4)
button11.grid(row=5,column=0,columnspan=3,sticky=tt.E+tt.W)
tic.resizable(0,0)
tic.mainloop()
