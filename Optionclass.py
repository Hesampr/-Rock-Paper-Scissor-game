
from random import choice as cs
class game :
    __choices = ['Rock','Paper','Scissors']

    
    __SelfChoice = cs(__choices)

    def UserChoice(self,Userch):
        self.__Userch = Userch
        

    def WhoWin(self):
        if self.__SelfChoice == "Rock":
            if  self.__Userch=="Rock":
                return "Draw"
            elif self.__Userch == "Paper":
                return "User win"
            else :
                return "Computer win"

        if self.__SelfChoice == "Paper" : 
            if self.__Userch=="Rock":
                return "Computer win"
            elif self.__Userch == "Paper":
                return "Draw"
            else :
                return "User win"

        if self.__SelfChoice == "Scissors" : 
            if self.__Userch=="Rock":
                return "User win" 
            elif self.__Userch == "Paper":
                return "Computer win"
            else :
                return "draw win"

    



