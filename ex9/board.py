# === CONSTANTS ===
BOARD_WIDTH = BOARD_HEIGHT = 7
EXIT_CORD = (round(BOARD_HEIGHT/2) - 1, BOARD_WIDTH)
EMPTY_CELL_CHAR = "_"

class Board:
    """
    A board class for the Rush Hour game.
    It has the following attributes:
    - board: A 2D array of characters representing the board
    - cars: A list of car objects
    - exit: The target cell of the board
    """

    def __init__(self):
        self.__load_board()

    def __load_board(self):
        self.__board = [[EMPTY_CELL_CHAR] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]
        self.__exit = None
        self.__cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        str = ""

        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                str += self.__board[i][j] + " "
            str += "\n"

        return str

    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        
        cords = []
        cords.append(self.target_location())
        
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                cords.append((i, j))
        
        return cords

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """

        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]

        legal_moves = []

        for car in self.__cars:
            car_moves = car.possible_moves()

            for move in car_moves.items():
                requirements = car.movement_requirements(move[0])
                
                if self.__is_board_meeting_requirements(requirements):    
                    legal_moves.append((car.get_name(), move[0], move[1]))

        return legal_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """

        return EXIT_CORD

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name of the car in coordinate, None if empty
        """

        if self.__is_same_cord(coordinate, EXIT_CORD):
            return self.__exit

        if not self.__is_cord_in_border(coordinate):
            return None

        val = self.__board[coordinate[0]][coordinate[1]]
        return None if val == EMPTY_CELL_CHAR else val

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        for existing_car in self.__cars:
            if existing_car.get_name() == car.get_name():
                return False

        # Checks that the car coordinates are inside the borders of the board
        coordinates = car.car_coordinates()
        for cord in coordinates:
            if cord[0] == self.target_location()[0] and cord[1] == self.target_location()[1]:
                if self.__exit != None:
                    return False
                continue

            if cord[0] < 0 or cord[0] >= BOARD_HEIGHT or cord[1] < 0 or cord[1] >= BOARD_WIDTH:
                return False

            if self.cell_content(cord) != None:
                return False

        self.__cars.append(car)
        self.__render_car(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        possible_moves = self.possible_moves()

        if not self.__move_in_move_list(name, movekey, possible_moves): 
            return False

        # We know that a car with name ${name} exists because of the above code
        car = self.__get_car_by_name(name)
        success = car.move(movekey)
        self.__render_car(car)
        return True

    # === UTILS ===
    def __is_cord_in_border(self, coordinate):
        """
        Checks if the given coordinates are inside the borders of the board
        """

        coordinates = self.cell_list()
        coordinates.remove(EXIT_CORD)
       
        for cord in coordinates:
            if self.__is_same_cord(cord, coordinate):
                return True
        
        return False
    
    def __render_car(self, car):
        """
        Re-renders the car in the board (removes previous renders)
        """

        # Removing previous render of the car
        for cord in self.cell_list():
            if self.cell_content(cord) == car.get_name():
                self.__board[cord[0]][cord[1]] = EMPTY_CELL_CHAR
        
        if self.__exit == car.get_name():
            self.__exit = None
        
        # re-rendering the car
        for cord in car.car_coordinates():
            if self.__is_same_cord(cord, EXIT_CORD):
                self.__exit = car.get_name()
            else:
                self.__board[cord[0]][cord[1]] = car.get_name()

    def __move_in_move_list(self, name, move_key, move_list):
        """
        Checks if the given move, ${move_key} for car ${name} is in
        the given list of moves
        """

        for move in move_list:
            if move[0] == name and move[1] == move_key:
                return True
        
        return False

    def __is_board_meeting_requirements(self, requirements):
        """
        Checks if the board meets the requirements, ${requirements}
        """
        
        for cell in requirements:
            if self.cell_content(cell) != None:
                return False

            if not self.__is_cord_in_border(cell) and \
                    not self.__is_same_cord(cell, EXIT_CORD):
                return False
        
        return True

    def __get_car_by_name(self, name):
        """
        Returns the car object with the name ${name}
        """

        for car in self.__cars:
            if car.get_name() == name:
                return car
        
        return None

    def __is_same_cord(self, cord1, cord2):
        """
        Checks if 2 coordinates are the same
        """

        return cord1[0] == cord2[0] and cord1[1] == cord2[1]