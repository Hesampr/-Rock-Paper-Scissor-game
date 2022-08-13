
from random import choice as cs
class game :
    __choices = ['Rock','Paper','Scissor']

    def __init__(self) -> None:
        self.__SelfChoice = cs(self.__choices)

    
    def Gamechoice(self):
        return self.__SelfChoice

    
        

    def WhoWin(Gamechoice,Userchoice):
        if Gamechoice == "Rock":
            if  Userchoice=="Rock":
                return "Draw"
            elif Userchoice == "Paper":
                return "You"
            else :
                return "Computer"

        if Gamechoice == "Paper" : 
            if Userchoice=="Rock":
                return "Computer"
            elif Userchoice == "Paper":
                return "Draw"
            else :
                return "You"

        if Gamechoice == "Scissor" : 
            if Userchoice=="Rock":
                return "You" 
            elif Userchoice == "Paper":
                return "Computer"
            else :
                return "Draw"

    



