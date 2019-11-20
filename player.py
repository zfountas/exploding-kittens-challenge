"""
Class player. Please write your name and email here.

This is what you need to change!
Feel free to do anything you want with this file, as long as it doesn't break
the rules of the game. We will figure it out :)
"""
import numpy as np
from base_player import BasePlayer

class Player(BasePlayer):
    def __init__(self,name):
        super().__init__(name)

    def turn(self):
        if self.hand[-1].name == 'Exploding Kitten':
            print('A player might explode..')
            for card in self.hand:
                if card.name == 'Defuse':
                    self.hand.pop()
                    card.effect(self,self)
    def skip(self):
        pass

    def take_turn_twice(self):
        self.turn()
        self.turn()

    def nope_prompt(self) -> bool:
        for card in self.hand:
            if card.name == "Nope":
                if input("Do you want to use your Nope card?").lower().startswith("y"):
                    return True
                else:
                    return False
        return False

    def insert_explode(self) -> int:
        #position = int(input("At which position from top do you want to insert Exploding Kitten back into the deck?"))
        position = np.random.randint(2)
        return position



#
