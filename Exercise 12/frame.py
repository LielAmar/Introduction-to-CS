import tkinter as tk

from gui_object import GUIObject


class Frame(GUIObject):
    """
    A Frame object
    """

    def __init__(self, root, rows: int, cols: int, row_weight=1, col_weight=1):

        if not isinstance(rows, int) or not isinstance(cols, int) or \
                not isinstance(row_weight, int) or not isinstance(col_weight, int):
            raise TypeError("rows, cols and weights must be integers")

        frame = tk.Frame(root)
        frame.grid_propagate(0)

        for i in range(rows): tk.Grid.rowconfigure(frame, i, weight=row_weight)
        for j in range(cols): tk.Grid.columnconfigure(frame, j, weight=col_weight)

        super().set_object(frame)