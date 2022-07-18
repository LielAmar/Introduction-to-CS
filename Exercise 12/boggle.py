try:
    import winsound
except ImportError:
    def playsound(frequency, duration): pass
else:
    def playsound(file, freq):
        winsound.PlaySound(file, freq)

import boggle_board_randomizer  as bbr
import ex12_utils               as utils

from typing     import List, Tuple
from constants  import *
from board      import Board
from button     import TogglableButton


class Boggle:
    """
    A boggle class representing a boggle game
    """
    
    def __init__(self):
        self.board = Board()

        self.__init_params()
        self.__init_logic()


    def __init_params(self):
        """
        Initializes the parameters of the game
        """
        
        self.__running = False
        
        self.__score = 0
        self.__used_words: List[str] = []
        self.__current_path: List[Tuple[int, int]] = []

        self.__words: List[str] = utils.read_file("boggle_dict.txt")
        self.__regenerate_letters()

    def __regenerate_letters(self):
        """
        Regenerates the board's letters
        """

        self.__letters: List[List[str]] = bbr.randomize_board()

    def __init_logic(self):
        """
        Initializes the logic of the game
        """

        self.widgets = self.board.get_widgets()

        # Updates the action button to "Start Game"
        self.widgets[ACTION].set_properties({
            PROP_COMMAND: self.__start_click
        })

        # Setting all button's command
        for i, row in enumerate(self.widgets[BUTTONS]):
            for j, button in enumerate(row):
                button.set_properties({
                    PROP_COMMAND: self.__command_wrapper(i, j)
                })


    # === ACTION BUTTON ===
    def __start_click(self):
        """
        Handles the click on the start button
        """
        
        self.board.update_all_buttons(selection=False, enabled=True, \
                letters=self.__letters)

        self.__score = 0
        self.__used_words = []

        self.widgets[SCORE].set_properties({
            PROP_TEXT: str(self.__score)
        })
        self.widgets[USED_WORDS].set_properties({
            PROP_TEXT: ""
        })
        self.widgets[ACTION].set_properties({
            PROP_TEXT: "Clear",
            PROP_COMMAND: self.__clear_click
        })

        self.__start_timer()

    def __clear_click(self):
        """
        Handles the click on the clear button
        """

        self.__current_path = []

        self.board.update_all_buttons(selection=False)

        playsound("sounds/clear.wav", 1)

    def __play_again_click(self):
        """
        Handles the click on the play again button
        """

        self.__regenerate_letters()
        self.widgets[TIMER].reset()

        self.__start_click()
    

    # === TIMER ===
    def __start_timer(self):
        """
        Starts the game timer
        """

        self.__running = True

        self.__tick()
    
    def __tick(self):
        """
        Ticks the game timer by 1 seconds
        """
        
        if self.__running:
            if not self.widgets[TIMER].tick():
                # If the timer is not over yet, we keep on ticking every 1s
                self.board.tk_after(1000, self.__tick)
            else:
                # If the timer is over, we stop the game and display the 
                # "Play Again" button
                self.widgets[ACTION].set_properties({ 
                    PROP_TEXT: "Play Again",
                    PROP_COMMAND: self.__play_again_click
                })
                
                self.board.update_all_buttons(selection=False, enabled=False)
                self.__running = False


    # === GAME BUTTONS ===
    def __command_wrapper(self, row, col):
        """
        Returns a function that handles the click on the given button
        """
        
        buttons = self.widgets[BUTTONS]

        def click():
            playsound("sounds/click.wav", 1)

            sender: TogglableButton = buttons[row][col]

            if sender.get_property(PROP_SELECTED):
                # If the button is now selected (after the click)

                # Updating the path
                self.__current_path.append((row, col))

                # If the updated path is not legal, we revert changes and return
                if not utils.is_legal_path(self.__letters, self.__current_path):
                    self.__current_path = self.__current_path[:-1]
                    
                    return buttons[row][col].set_properties({
                        PROP_SELECTED: False
                    })
                
                # If the path is valid we checking if we got a valid word.
                # If we have not found the word prior, we add it to our word bank

                result = utils.is_valid_path(self.__letters, self.__current_path, \
                        self.__words)

                if result:
                    if result not in self.__used_words:
                        self.__score += utils.get_path_score(self.__current_path)
                        self.widgets[SCORE].set_properties({ PROP_TEXT: str(self.__score) })

                        self.__used_words += [result]
                        
                        text = ", ".join(self.__used_words)
                        # for i in range(25, len(text), 25):
                        #     comma = text.find(", ", i)
                        #     text = text[:i+comma] + "\n" + text[comma+i:]

                        self.widgets[USED_WORDS].set_properties({ PROP_TEXT: text })

                        playsound("sounds/success.wav", 1)

            else:
                # If the button is not selected anymore (after the click)
                index = self.__current_path.index((row, col))
                canceled = self.__current_path[index:]
                self.__current_path = self.__current_path[:index]

                # Unselecting all the buttons that came after the clicked one
                for (r, c) in canceled:
                    buttons[r][c].set_properties({ PROP_SELECTED: False })

        return click


    def start(self):
        """
        Starts the game
        """
       
        self.board.start_gui()


if __name__ == "__main__":
    Boggle().start()