# === CONSTANTS ===
BOARD_WIDTH = BOARD_HEIGHT = 7
EXIT_CORD = (round(BOARD_HEIGHT/2) - 1, BOARD_WIDTH)

EMPTY_CELL_CHAR = "_"
VALID_NAMES = ["Y","B","O","G","W","R"]

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.__load_board()

    def __load_board(self):
        self.__board = [EMPTY_CELL_CHAR * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                print(self.__board[i][j], end = " ")
            print()

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
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
        pass

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

        val = self.__board[coordinate[0]][coordinate[1]]
        return None if val == EMPTY_CELL_CHAR else val

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        # Checks the car's name is valid
        if not car.get_name() in VALID_NAMES:
            return False

        # Checks that the car coordinates are inside the borders of the board
        coordinates = car.car_coordinates()
        for cord in coordinates:
            if cord[0] == self.target_location()[0] and cord[1] == self.target_location()[1]:
                continue

            if cord[0] < 0 or cord[0] >= BOARD_HEIGHT or cord[1] < 0 or cord[1] >= BOARD_WIDTH:
                return False
        
        

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass
