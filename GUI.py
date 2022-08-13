#tkinter is a library for creating graphical user interface
import tkinter as tk
import tkinter.messagebox as mb

#OptionClass is a class I made for game rules
import Optionclass 


#start setting
Root = tk.Tk()
Root.title("Rock Paper Scissors game")
Root.resizable(width=False ,height=False)
Root.geometry("400x500")
Root.config(bg="#29465B")




#Backgrounds

Rockbg = tk.PhotoImage(file = './Rock.png')
Paperbg = tk.PhotoImage(file = './Paper.png')
Scissorbg = tk.PhotoImage(file = './Scissor.png')
Playbg = tk.PhotoImage(file  = "./Play.png")



#Definition

GameDesicion = tk.StringVar()
USerDesicion = tk.StringVar()
Winner= tk.StringVar()



#Functions 

def Playfunc():
    try:
        obj1 = Optionclass.game()
        temp = obj1.Gamechoice()
        GameDesicion.set(temp)
        
        mb.showinfo("Choice","Computer decided ,Please select")
                
    except:
        pass




def Rockfunc():
    USerDesicion.set("Rock") 
    temp=GameDesicion.get()
    if temp!="":     
        Winnerfunc()
    else:
        mb.showerror("Decision error","The computer didn't decide ,Please click on the play icon ")

def Paperfunc():
    USerDesicion.set("Paper")
    temp=GameDesicion.get()
    if temp!="":     
        Winnerfunc()
    else:
        mb.showerror("Decision error","The computer didn't decide ,Please click on the play icon ")

def Scissorsfunc():
    USerDesicion.set("Scissors")
    temp=GameDesicion.get()
    if temp!="":     
        Winnerfunc()
    else:
        mb.showerror("Decision error","The computer didn't decide ,Please click on the play icon ")

def Winnerfunc():
    temp1 = GameDesicion.get()
    temp2 = USerDesicion.get()
    winnerstr =Optionclass.game.WhoWin(temp1,temp2)
    Reswinner = f"Computer: {temp1}"+ f" You: {temp2}"
    if winnerstr!="Draw":
        Reswinner+= f"\n{winnerstr} won"
    else:
        Reswinner+=f"\n Draw"

    Winner.set(Reswinner)
    Root.after(4000,Root.destroy)





#Buttons

RockButton = tk.Button(Root,image=Rockbg , height=70,width=70,command=Rockfunc  )
RockButton.place(x=60,y=220)

PaperButton = tk.Button(Root,image=Paperbg, height=70,width=70,command=Paperfunc)
PaperButton.place(x=160,y=220)

ScissorsButton = tk.Button(Root,image = Scissorbg , height=70,width=70 ,command=Scissorsfunc)
ScissorsButton.place(x=260,y=220)

PlayButton= tk.Button(Root,image=Playbg, height=70,width=100 , command=lambda :Playfunc() )
PlayButton.place(x=145,y=100)



#Labels

ResLabel = tk.Label(Root,width=31,height=2,bg="#E9AB17",fg="#8B0000",textvariable=Winner,font=("Arial",13))
ResLabel.place(x=60,y=340)






mb.showinfo("Click","Click on the play icon")

Root.mainloop()