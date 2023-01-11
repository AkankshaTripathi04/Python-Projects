import math
import random
#first we write the player class, which will have the letter that the player is playing and 
# get move function that will get the next move of the palyer, this is a general class 
class Players:
    def __init__(self, letter):
         self.letter = letter

    def get_move(self, game):
        pass

#Here we have the child classes the computer class for when the computers paly and humans class for when teh humans play 
class RandomComputerPlayer(Players):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move():
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Players):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move():
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input a valis square.")
            try:
                val = int(square)
            #we are going to check if the number is valid 
                if val not in game.available_moves:
                    raise ValueError
            except ValueError:
                print("Invalid square! make a valid move.")
                
        return val              



