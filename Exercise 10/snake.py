from constants import *

from board_object import *

from typing import Optional

class Snake(BoardObject):
    """
    A class representing a single snake object with:
    x, y, color, length and direction
    """

    def __init__(self, x: int, y: int, color: str = COLOR_BLACK,
            length: int = 3, direction: Direction = DIRECTIONS["Up"]):

        super().__init__(x, y, color)

        self.__length = length
        self.__direction = direction

        self.__head = SnakeNode(x, y, color)


        self.__tail = self.__head

        # Adds all initial nodes to the tail
        for i in range(length - 1):
            new_tail = SnakeNode(x, y - i - 1, color)
            self.__tail.set_next(new_tail)
            new_tail.set_prev(self.__tail)
            self.__tail = self.__tail.get_next()


    def add_length(self, length: int) -> bool:
        """
        Adds ${length} to the snake's length 
        """
        self.__length += length
        return True

    def change_direction(self, new_direction) -> bool:
        """ 
        Tries to change the snake's direction to the given
        direction, only if those 2 are related (is allowed switch)
        """

        if not self.__direction.is_allowed_switch(new_direction):
            return False
        
        self.__direction = new_direction
        return True

    def move(self):
        """
        Moves the snake in it's direction by:
        - Adding a new head calculated through direction
        - Removing the tail of the snake

        Returns the removed tail for other functions to use as necessary
        """

        head_x, head_y = self.__head.get_cord()
        x_diff, y_diff = self.__direction.get_diff()

        # Sets new head
        new_head = SnakeNode(head_x + x_diff, head_y + y_diff, super().get_color())
        new_head.set_next(self.__head)
        self.__head.set_prev(new_head)
        self.__head = new_head

        # Sets new tail
        old_tail = self.__tail
        old_tail_prev = old_tail.get_prev()

        if old_tail_prev is not None:
            old_tail_prev.set_next(None)
            self.__tail = old_tail_prev
        else:
            self.__tail = self.__head

        old_tail.set_prev(None)
        return old_tail 

    def tick(self) -> bool:
        """
        A single snake tick:
        - Moves the snake in it's direction
        - If the wanted length of the snake is not the actual length
          we add a new node
        """
        
        old_tail = self.move()

        if len(self.__head) < self.__length:
            self.__tail.set_next(old_tail)
            old_tail.set_prev(self.__tail)
            self.__tail = old_tail
        
        return False

    def draw(self):
        """
        Returns all the coordinates of the snake
        that should be drawn
        """

        lst: list[tuple[int, int, str]] = []

        pointer = self.__head

        while pointer is not None:
            lst.append((pointer.get_cord()[0], pointer.get_cord()[1], pointer.get_color()))

            pointer = pointer.get_next()

        return lst


class SnakeNode(BoardObject):
    """
    A class representing a single snake node object with:
    x, y and color
    
    It acts as a custom linked-list
    """

    def __init__(self, x: int, y: int, color: str):
        super().__init__(x, y, color)

        self.__next = None
        self.__prev = None

    def __len__(self):
        length = 1

        if self.__next is not None:
            length += len(self.__next)
        
        return length


    def set_next(self, node):
        self.__next = node
    
    def get_next(self):
        return self.__next
    
    def set_prev(self, node):
        self.__prev = node
    
    def get_prev(self):
        return self.__prev