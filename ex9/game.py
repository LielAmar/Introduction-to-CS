from car import *
from board import *
from helper import *

class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """

        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """

        print(self.__board)
        print("===========================")

        user_input = input("""
            Enter the color of the car you want to move,
            and the direction you want to move in (e.g., (R,u)):
            """)
        if len(user_input) != 3 or user_input[1] != ",":
            print("""
                Invalid input. Please enter a valid color and direction.
            """)
            return

        color, direction = user_input.split(",")
        
        possible_moves = self.__board.possible_moves()
        
        if not self.__color_has_move(color, direction, possible_moves):
            print("""
                Car not found or recived an invalid/impossible direction.
                """)
            return

        board.move_car(color, direction)
        return

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        moves = 0

        while board.cell_content(board.target_location()) == None:
            moves += 1
            self.__single_turn()

        print("Well done! You finished the game in {} moves!".format(str(moves)))


    # === UTILS ===
    def __color_has_move(self, color, direction, moves):
        for move in moves:
            if move[0] == color and move[1] == direction:
                return True
        return False


import sys

VALID_NAMES = ["R","G","W","O","B","Y"]

if __name__== "__main__":
    script, path_to_json = sys.argv

    car_data = load_json(path_to_json)
    board = Board()

    for car in car_data.items():
        if car[0] in VALID_NAMES:
            name = car[0]
            length = car[1][0]
            location = (car[1][1][0], car[1][1][1])
            orientation = car[1][2]

            car = Car(name, length, location, orientation)
            board.add_car(car)

    game = Game(board)
    game.play()
