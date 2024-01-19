import math
import random

class Player:
    def __init__(self, letter): #letter x or y
        self.letter = letter
        
    def get_move(self, game):