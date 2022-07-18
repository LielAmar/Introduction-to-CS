import tkinter as tk

from typing import Optional, Any


class GUIObject:
    """
    An abstract class for GUI Objects to implement
    """

    def __init__(self):
        self.__object


    def get_object(self):
        """
        Returns the raw tkinter object
        """

        return self.__object

    def set_object(self, object):
        """
        Sets the raw tkinter object
        """

        self.__object = object
    
    def set_position(self, row=-1, column=-1, rowspan=1, columnspan=1, \
            sticky=tk.NSEW):
        """
        Sets the new position of the object in a grid/frame
        """
        
        if row >= 0 and column >= 0:
            self.__object.grid(row=row, column=column, rowspan=rowspan, \
                    columnspan=columnspan, sticky=sticky)
        else:
            self.pack()

    def pack(self, orientation=None, padx=0, pady=0):
        """
        Packs the object in the parent frame
        """
        
        if orientation: self.__object.pack(side=orientation, padx=padx, pady=pady)
        else: self.__object.pack(padx=padx, pady=pady)


    # === PROPERTIES ===
    def get_property(self, property: str) -> Optional[Any]:
        """
        Returns the value of a certain property in the tkinter object
        """

        if self.has_property(property):
            return self.__object.cget(property)

    def has_property(self, property: str) -> bool:
        """
        Retruns whether the tkinter object has the property ${property}
        """
        
        return property in self.__object.config()

    def set_property(self, property: str, value: Any):
        """
        Sets the value of a certain property in the tkinter object
        """

        if self.has_property(property):
            self.__object.config(**{property: value})

    def set_properties(self, kwargs):
        """
        Sets multiple properties in the tkinter object
        """
        
        for key, value in kwargs.items():
            self.set_property(key, value)