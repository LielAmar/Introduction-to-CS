import tkinter as tk

from constants import *
from gui_object import GUIObject


class Button(GUIObject):
    """
    An object to wrap a button in the GUI, using tkinter
    """
    
    def __init__(self, root, text=DEFAULT_BUTTON_TEXT):
        if not isinstance(text, str):
            raise TypeError("${text} must be a string")

        self.__command = None
        
        button = tk.Button(root, text=text, command=self.click)
        super().set_object(button)
    

    def click(self) -> bool:
        """
        Handles the click event of a button
        If the button was able to process the click, it retuns True
        """
        
        if self.__command:
            self.__command()

            return True
        
        return False


    def get_property(self, property: str):
        """
        Overrides the parent's get_property function to add support to
        command and enabled properties
        """
        
        if property == PROP_COMMAND:
            return self.__command
        elif property == PROP_ENABLED:
            return super().get_object().cget("state") == "normal"
        else:
            return super().get_property(property)

    def set_property(self, property, value):
        """
        Overrides the parent's set_property function to add support to
        command and enabled properties
        """

        if property == PROP_COMMAND:
            self.__command = value
        elif property == PROP_ENABLED:
            if value:
                super().set_properties({
                    PROP_BACKGROUND: BUTTON_NORMAL_BG_COLOR,
                    PROP_FOREGROUND: BUTTON_NORMAL_FG_COLOR
                })
            else:
                super().set_properties({
                    PROP_BACKGROUND:          BUTTON_DISABLED_BG_COLOR,
                    PROP_DISABLED_FOREGROUND: BUTTON_DISABLED_FG_COLOR
                })

            super().get_object().config(state=("normal" if value else "disabled"))
        else:
            super().set_property(property, value)


class TogglableButton(Button):
    """
    A TogglableButton inheriting from Button.
    It has an option to stay toggled when pressed.
    """
    
    def __init__(self, root, text="?"):
        super().__init__(root, text)

        self.__selected = False
        super().set_properties({
            PROP_BACKGROUND: BUTTON_NORMAL_BG_COLOR,
            PROP_FOREGROUND: BUTTON_NORMAL_FG_COLOR
        })


    def click(self):
        """
        Overrides ${Button}'s click function to also apply the selection
        whenever the button is clicked
        """

        self.set_properties({ PROP_SELECTED: not self.get_property(PROP_SELECTED) })

        # If the click was not successful, we want to revert the selection
        if not super().click():
            self.set_properties({ PROP_SELECTED: not self.get_property(PROP_SELECTED) })


    def get_property(self, property: str):
        """
        Overrides the parent's get_property function to add support to
        the selected property
        """
        
        if property == PROP_SELECTED:
            return self.__selected
        else:
            return super().get_property(property)

    def set_property(self, property, value):
        """
        Overrides the parent's set_property function to add support to
        the selected property
        """

        if property == PROP_SELECTED:
            self.__selected = value

            super().set_properties({
                PROP_BACKGROUND: BUTTON_SELECTED_BG_COLOR if value else BUTTON_NORMAL_BG_COLOR,
                PROP_FOREGROUND: BUTTON_SELECTED_FG_COLOR if value else BUTTON_NORMAL_FG_COLOR
            })
        else:
            super().set_property(property, value)