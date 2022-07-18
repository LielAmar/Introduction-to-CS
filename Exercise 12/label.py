import tkinter as tk

from constants  import *
from gui_object import GUIObject


class Label(GUIObject):
    """
    A Label object to display text
    """

    def __init__(self, root, prefix="", wraplength=-1): 
        if not isinstance(prefix, str):
            raise TypeError("${prefix} must be a string")

        self.__prefix = prefix

        label = tk.Label(root, text = prefix + "", wraplength=wraplength, justify="left")
        super().set_object(label)


    def set_property(self, property, value):
        """
        Overrides the parent's set_property function to add support to
        the text property
        """

        if property == PROP_TEXT:
            value = self.__prefix + value

        super().set_property(property, value)