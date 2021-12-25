# === CONSTANTS ===
VERTICAL = 0
HORIZONTAL = 1

MAX_VERTICAL_VALUE = MAX_HORIZONTAL_VALUE = 7
MIN_VERTICAL_VALUE = MIN_HORIZONTAL_VALUE = 0

UP = "u"
DOWN = "d"
LEFT = "l"
RIGHT = "r"

class Car:
    """
    A car object representing a 2D car that can only move in one axis.
    It has the following attributes:
    - name: The cars name
    - length: The cars length
    - location: The cars head
    - orientation: The orientation of the car
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """

        cords = []

        for i in range(self.__length):
            if self.__orientation == VERTICAL:
                cords.append((self.__location[0] + i, self.__location[1]))
            else:
                cords.append((self.__location[0], self.__location[1] + i))

            # if self.orientation == VERTICAL:
            #     cords.append(self.location[0] + i, self.location[1])
            # else:
            #     cords.append(self.location[0] + i, self.location[1])

        return cords

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        if self.__orientation == VERTICAL:
            return {UP: "cause the car to fly and reach the Moon",
                    DOWN: "cause the car to dig and reach the core of Earth"}
        
        return {LEFT: "cause the car can ride left towards the seas",
                RIGHT: "cause the car can ride in the right path"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        min_cord = self.__location

        possible_moves = []

        if self.__orientation == VERTICAL:
            if movekey == UP:
                possible_moves.append((min_cord[0] - 1, min_cord[1]))
            elif movekey == DOWN:
                possible_moves.append((min_cord[0] + self.__length, min_cord[1]))
        elif self.__orientation == HORIZONTAL:
            if movekey == LEFT:
                possible_moves.append((min_cord[0], min_cord[1] - 1))
            elif movekey == RIGHT:
                possible_moves.append((min_cord[0], min_cord[1] + self.__length))

        return possible_moves

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        
        # TODO fix this shit

        if movekey not in self.possible_moves():
            return False
        
        possible_moves = self.movement_requirements(movekey)
        
        if len(possible_moves) == 0:
            return False
        
        if movekey == UP or movekey == LEFT:
            self.__location = possible_moves[0]
        elif movekey == DOWN:
            self.__location = (self.__location[0] + 1, self.__location[1])
        elif movekey == RIGHT:
            self.__location = (self.__location[0], self.__location[1] + 1)
        
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        
        return self.__name