from board_object import *

from constants import *

class Apple(BoardObject):
    """
    A class representing a single apple object with:
    x, y, color and score
    """

    def __init__(self, x: int, y: int, color: str = COLOR_GREEN,
            score: int = 1):
        super().__init__(x, y, color)

        self.__score = score

    def get_score(self):
        return self.__score

    def draw(self):
        return [(super().get_cord()[0], super().get_cord()[1], super().get_color())]

    def tick(self) -> bool:
        pass
