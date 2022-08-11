#tkinter is a library for creating graphical user interface
import tkinter as tk

import tkinter.messagebox as mb
from turtle import pd 

import Optionclass 


#start setting
Root = tk.Tk()
Root.title("Rock Paper Scissors game")
Root.resizable(width=False ,height=False)
Root.geometry("400x500")
Root.config(bg="#29465B")




#Backgrounds
Rockbg = tk.PhotoImage(file = 'Rock.png')
Paperbg = tk.PhotoImage(file = 'Paper.png')
Scissorsbg = tk.PhotoImage(file = 'Scissors.png')
Playbg = tk.PhotoImage(file  = "Play.png")



#Functions 

GameDesicion = tk.StringVar()
USerDesicion = tk.StringVar()
Winner= tk.StringVar()
Winner.set("please choose")
# defaultText=tk.StringVar()

def Playfunc():
    try:
        Winner.set("please choose")
        mb.showinfo("choice","Computer decided , please choose ")
        obj1 = Optionclass.game()
        temp = obj1.Gamechoice()
        GameDesicion.set(temp)
                

    except:
        pass

def Rockfunc():
    USerDesicion.set("Rock")
    Winnerfunc()

def Paperfunc():
    USerDesicion.set("Paper")
    Winnerfunc()

def Scissorsfunc():
    USerDesicion.set("Scissors")
    Winnerfunc()

def Winnerfunc():
    temp1 = GameDesicion.get()
    temp2 = USerDesicion.get()
    winnerstr =Optionclass.game.WhoWin(temp1,temp2)
    Reswinner = f"Computer: {temp1}"+ f" and you: {temp2}"
    if winnerstr!="Draw":
        Reswinner+= f"\n{winnerstr} winned"
    else:
        Reswinner+=f"\n drawed"
    
    Winner.set(Reswinner)



#Buttons

RockButton = tk.Button(Root,image=Rockbg , height=70,width=70,command=Rockfunc  )
RockButton.place(x=60,y=220)

PaperButton = tk.Button(Root,image=Paperbg, height=70,width=70,command=Paperfunc)
PaperButton.place(x=160,y=220)

ScissorsButton = tk.Button(Root,image = Scissorsbg , height=70,width=70 ,command=Scissorsfunc)
ScissorsButton.place(x=260,y=220)

PlayButton= tk.Button(Root,image=Playbg, height=70,width=100 , command=lambda :Playfunc() )
PlayButton.place(x=145,y=100)



#Labels

ResLabel = tk.Label(Root,width=31,height=2,bg="#E9AB17",textvariable=Winner,font=("Arial",13))
ResLabel.place(x=60,y=340)




mb.showinfo("click","click on play icon")








Root.mainloop()