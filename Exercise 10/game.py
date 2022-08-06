from game_parameters import *
from game_display import *

from snake import *
from bomb import *
from apple import *
from board import *
from constants import *

# === CONSTANTS ===
INIT_SNAKE_X, INIT_SNAKE_Y = 10, 10

class Game:
    """
    A class representing a single game object with:
    board and score
    """

    def __init__(self):
        snake = Snake(INIT_SNAKE_X, INIT_SNAKE_Y)

        self.__board = Board(WIDTH, HEIGHT, snake)
        self.__score = 0

    def single_turn(self, key: Optional[str]):
        state, score_to_add = self.__board.tick(key)

        self.__score += score_to_add
        return state

    def draw(self, gd: GameDisplay):
        for cell in self.__board.draw():
            gd.draw_cell(cell[0], cell[1], cell[2])

    def get_score(self):
        return self.__score

    



    

    def get_pixels(self):
        # dict = { "black": [], "green": [], "red": [], "orange": []}
        dict = {}
        
        for item in self.__board.draw():
            if item[2] not in dict:
                dict[item[2]] = []
            dict[item[2]].append((item[0], item[1]))

        return dict

    def set_data(self, apples, bomb):
        self.__board.set_data(apples, bomb)