#tkinter is a library for creating graphical user interface

from logging import root
import tkinter as tk
from turtle import bgcolor



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


#Buttons

RockButton = tk.Button(Root,image=Rockbg , height=70,width=70 )
RockButton.place(x=60,y=220)

PaperButton = tk.Button(Root,image=Paperbg, height=70,width=70)
PaperButton.place(x=160,y=220)

ScissorsButton = tk.Button(Root,image = Scissorsbg , height=70,width=70 )
ScissorsButton.place(x=260,y=220)

PlayButton= tk.Button(Root,image=Playbg, height=70,width=100 )
PlayButton.place(x=145,y=100)




#Labels

ResLabel = tk.Label(Root,width=39,height=3,bg="#E9AB17")
ResLabel.place(x=60,y=340)













Root.mainloop()