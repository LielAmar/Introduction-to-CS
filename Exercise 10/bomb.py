from board_object import *

from constants import *

class Bomb(BoardObject):
    """
    A class representing a single bomb object with:
    x, y, color, timer, radius and blast_color
    """

    def __init__(self, x: int, y: int, color: str = COLOR_RED,
            timer: int = 1, radius: int = 1, blast_color: str = COLOR_ORANGE):
        super().__init__(x, y, color)

        self.__timer = timer
        self.__radius = radius
        self.__blast_color = blast_color

        self.__current_radius = -1

    def draw(self):
        """
        Returns all the coordinates of the bomb & the blast
        that should be drawn
        """

        x, y = super().get_cord()

        if self.__timer != 0:
            return [(x, y, super().get_color())]
        
        lst = []
        for u in range(x - self.__current_radius, x + self.__current_radius + 1, 1):
            for v in range(y - self.__current_radius, y + self.__current_radius + 1, 1):
                if abs(x - u) + abs(y - v) == self.__current_radius:
                    lst.append((u, v, self.__blast_color))

        return lst

    def tick(self) -> bool:
        """
        A single bomb tick:
        - Updates the timer if it's not at 0
        - If the timer reached 0, updates the current radius
        
        Returns True if the bomb's life-span has ended and should be deleted
        """
        
        if self.__timer != 0:
            self.__timer -= 1
        
        # If the timer reaches 0, we want to render the bomb's blast instead of the bomb
        if self.__timer <= 0:
            if self.__current_radius >= self.__radius:
                return True

            if self.__current_radius < self.__radius:
                self.__current_radius += 1
        
        return False