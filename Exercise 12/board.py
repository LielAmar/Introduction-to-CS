import tkinter as tk
from tkinter.constants import TOP

from typing     import Dict, List, Tuple

from constants  import *
from cursors    import Cursors
from gui_object import GUIObject
from frame      import Frame
from label      import Label
from timer      import Timer
from button     import Button, TogglableButton


class Board:
    """
    A Board object representing the GUI of the game
    This object has no game-logic associated with it and only contains the
    visual elements wrappers
    """

    def __init__(self):
        """
        Initiates a new Board object
        """

        self.__root = tk.Tk()
        self.__root.title("Best Boggle Game 100/100 ez clap")
        self.__root.config(bg=GUI_BACKGROUND)
        self.__root.maxsize(GUI_WIDTH, GUI_HEIGHT)
        self.__root.minsize(GUI_WIDTH, GUI_HEIGHT)
        self.__root.resizable(False, False)

        self.__cursors = Cursors()
        self.__buttons: List[List[Button]] = [[] for _ in range(BOARD_SIZE)]
        
        # Initiates the GUI
        self.__create_top_frame()
        self.__create_game_board()
        self.__create_bottom_frame()


    def __create_top_frame(self):
        """
        Creates the top label (Score & Timer)
        """

        frame_wrapper = Frame(self.__root, rows=1, cols=2)
        frame_wrapper.set_properties({
            PROP_HIGHLIGHTTHICKNESS: 0,
            PROP_WIDTH:  GUI_WIDTH-GUI_MARGIN,
            PROP_HEIGHT: TOP_FRAME_HEIGHT
        })

        self.__score_wrapper = Label(frame_wrapper.get_object(), prefix="Score: ")
        self.__score_wrapper.set_position(row=0, column=0)
        self.__score_wrapper.set_properties({
            PROP_TEXT:       "0",
            PROP_BACKGROUND: GUI_BACKGROUND,
            PROP_ANCHOR:     LEFT,
            PROP_FONT:       LABEL_FONT,
            PROP_FOREGROUND: LABEL_TEXT_COLOR
        })

        self.__timer_wrapper = Timer(frame_wrapper.get_object(), prefix="Timer: ")
        self.__timer_wrapper.set_position(row=0, column=1)
        self.__timer_wrapper.set_properties({
            PROP_BACKGROUND: GUI_BACKGROUND,
            PROP_ANCHOR:     RIGHT,
            PROP_FONT:       LABEL_FONT,
            PROP_FOREGROUND: LABEL_TEXT_COLOR
        })

        frame_wrapper.pack()

    def __create_game_board(self):
        """
        Creates the game board (Middle layer)
        """

        frame_wrapper = Frame(self.__root, BOARD_SIZE, BOARD_SIZE)
        frame_wrapper.set_properties({
            PROP_HIGHLIGHTTHICKNESS: 0,
            PROP_WIDTH:  GUI_WIDTH-GUI_MARGIN,
            PROP_HEIGHT: MID_FRAME_HEIGHT
        })

        for i in range(BOARD_SIZE**2):
            row, col = self.parse_index_to_coords(i)

            button = TogglableButton(frame_wrapper.get_object())
            button.set_position(row, col)
            button.set_properties({
                PROP_CURSOR: next(self.__cursors),
                PROP_FONT: BUTTON_FONT,
                PROP_ENABLED: False,
            })

            self.__buttons[row].append(button)

        frame_wrapper.pack()

    def __create_bottom_frame(self):
        """
        Creates the bottom label (Score & Timer)
        """

        frame_wrapper = Frame(self.__root, 1, 1)
        frame_wrapper.set_properties({
            PROP_HIGHLIGHTTHICKNESS: 0,
            PROP_WIDTH:  GUI_WIDTH-GUI_MARGIN,
            PROP_HEIGHT: ACT_FRAME_HEIGHT
        })

        self.__action_wrapper = Button(frame_wrapper.get_object(), "Start")
        self.__action_wrapper.set_position(0, 0)
        self.__action_wrapper.set_properties({
            PROP_FONT: ACTION_BUTTON_FONT
        })

        frame_wrapper.pack("top", pady=ACT_FRAME_PAD)


        frame_wrapper = Frame(self.__root, 2, 1)
        frame_wrapper.set_properties({
            PROP_BACKGROUND: GUI_BACKGROUND,
            PROP_HIGHLIGHTTHICKNESS: 0,
            PROP_WIDTH:  GUI_WIDTH-GUI_MARGIN,
            PROP_HEIGHT: BANK_FRAME_HEIGHT
        })

        self.__used_words_prefix_wrapper = Label(frame_wrapper.get_object(), \
                prefix="Words Bank: ")
        self.__used_words_prefix_wrapper.set_position(row=0, column=0, sticky=UP + LEFT)
        self.__used_words_prefix_wrapper.set_properties({
            PROP_TEXT:       "",
            PROP_BACKGROUND: GUI_BACKGROUND,
            PROP_ANCHOR:     LEFT,
            PROP_FONT:       LABEL_FONT,
            PROP_FOREGROUND: LABEL_TEXT_COLOR
        })

        self.__used_words_wrapper = Label(frame_wrapper.get_object(), prefix="", \
                wraplength=GUI_WIDTH-GUI_MARGIN)
        self.__used_words_wrapper.set_position(row=1, column=0, sticky=UP + LEFT)
        self.__used_words_wrapper.set_properties({
            PROP_TEXT:       "",
            PROP_BACKGROUND: "white",
            PROP_ANCHOR:     UP+LEFT,
            PROP_FONT:       LABEL_FONT_UNFOCUSED,
            PROP_FOREGROUND: LABEL_TEXT_COLOR,
            PROP_HEIGHT: 7,
            PROP_WIDTH: GUI_WIDTH-GUI_MARGIN
        })

        frame_wrapper.pack("top")

    def get_widgets(self) -> Dict[str, GUIObject]:
        """
        Returns a dictionary with all widgets of the GUI
        """

        return {
            SCORE:      self.__score_wrapper,
            TIMER:      self.__timer_wrapper,
            BUTTONS:    self.__buttons,
            ACTION:     self.__action_wrapper,
            USED_WORDS: self.__used_words_wrapper
        }

    def update_all_buttons(self, selection: bool=None, enabled: bool=None, \
            letters=None):
        """
        Updates all buttons in the GUI with the given data
        """

        for i, row in enumerate(self.__buttons):
            for j, button in enumerate(row):

                if selection != None:
                    if not isinstance(selection, bool):
                        raise TypeError("${selection} must be a boolean")
                    
                    button.set_properties({ PROP_SELECTED: selection })


                if enabled != None:
                    if not isinstance(enabled, bool):
                        raise TypeError("${enabled} must be a boolean")

                    button.set_properties({ PROP_ENABLED: enabled })

                if letters != None:
                    if not isinstance(letters, List):
                        raise TypeError("${letters} must be a 2D array of strings")

                    button.set_properties({ PROP_TEXT: letters[i][j] })

    def tk_after(self, ms=1000, fn=lambda: None) -> None:
        """
        Calls the given function after the given amount of milliseconds
        """

        if not callable(fn):
            raise TypeError("${fn} must be a function")

        self.__root.after(ms,fn)
    
    def parse_index_to_coords(self, i) -> Tuple[int, int]:
        """
        Parses the given index into coordinates in a board of size ${BOARD_SIZE}
        """

        if not isinstance(i, int):
            raise TypeError("${i} must be an integer")

        return (i//BOARD_SIZE, i % BOARD_SIZE)


    def start_gui(self):
        """
        Starts-up the GUI
        """

        self.__root.mainloop()