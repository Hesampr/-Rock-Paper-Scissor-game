
from random import choice as cs
class game :
    __choices = ['Rock','Paper','Scissors']

    def __init__(self) -> None:
        self.__SelfChoice = cs(self.__choices)

    
    def Gamechoice(self):
        return self.__SelfChoice

    def UserChoice(self,Userch):
        self.__Userch = Userch
        

    def WhoWin(Gamechoice,Userchoice):
        if Gamechoice == "Rock":
            if  Userchoice=="Rock":
                return "Draw"
            elif Userchoice == "Paper":
                return "User"
            else :
                return "Game"

        if Gamechoice == "Paper" : 
            if Userchoice=="Rock":
                return "Game"
            elif Userchoice == "Paper":
                return "Draw"
            else :
                return "User"

        if Gamechoice == "Scissors" : 
            if Userchoice=="Rock":
                return "User" 
            elif Userchoice == "Paper":
                return "Game"
            else :
                return "Draw"

    



