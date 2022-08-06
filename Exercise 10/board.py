from game_parameters import *

from constants import *

from apple import *
from snake import *
from bomb import *

class Board:
    """ 
    An object representing a single game board with properties:
    width, height and snake 
    """

    def __init__(self, width: int, height: int, snake: Snake):
        self.__width = width
        self.__height = height
        
        # Setting the snake
        self.__snake: Snake = snake

        # Creating the apples
        self.__apples: list[Apple] = []

        # Creating the first bomb
        self.__add_bomb()

        # for i in range(AMOUNT_OF_APPLES):
        self.__add_apples()


    def __add_apples(self) -> bool:
        """
        Makes sure there are 3 apples on the board at all times
        If we can't place another apple, we return False 
        """

        taken_cells = 0
        taken_cells += len(self.__snake.draw())
        taken_cells += len(self.__bomb.draw())

        for apple in self.__apples:
            taken_cells += len(apple.draw())

        if taken_cells >= self.__width * self.__height:
            return False

        while len(self.__apples) != AMOUNT_OF_APPLES:
            apple_x, apple_y, apple_score = get_random_apple_data()
            apple = Apple(apple_x, apple_y, COLOR_GREEN, apple_score)

            if not self.__is_cord_in_bounds(apple.get_cord()):
                continue

            if not self.__is_cord_empty(apple.get_cord()):
                continue

            self.__apples.append(apple)
        
        return True
    
    def __add_bomb(self) -> bool:
        """
        Makes sure there's a bomb on the board at all times
        """

        bomb_x, bomb_y, bomb_radius, bomb_timer = get_random_bomb_data()

        while not self.__is_cord_in_bounds((bomb_x, bomb_y)) and \
                not self.__is_cord_empty((bomb_x, bomb_y)):
            bomb_x, bomb_y, bomb_radius, bomb_timer = get_random_bomb_data()

        self.__bomb = Bomb(bomb_x, bomb_y, COLOR_RED, bomb_timer, bomb_radius)
        return True


    def tick(self, key: Optional[str]):
        """
        Handles a single board tick:
        - Updates the snake's direction according to the input
        - Checks if the game has been won
        - Updates the snakes location
        - Updates the bomb's timer
        - Checks for collisions

        This function returns the current game state (keep playing, win or lose) and
        the amount of points the user should be granted by the end of the tick
        """
        
        # Handling key input
        if key in DIRECTIONS:
            self.__snake.change_direction(DIRECTIONS[key])

        score_to_add = 0

        # Ticking the snake
        self.__snake.tick()

        state, score_to_add_tmp = self.__check_snake_collisions()
        score_to_add += score_to_add_tmp

        # Checking if we should reset the bomb after this tick
        if self.__bomb.tick():
            self.__add_bomb()

        if state == LOSE:
            return state, score_to_add

        state, score_to_add_tmp = self.__check_bomb_collisions()
        score_to_add += score_to_add_tmp
        if state == LOSE:
            return state, score_to_add

        # Adding the missing apples
        # We check if the game was won because we can't add any more apples
        if not self.__add_apples():
            return (WIN, 0)

        return state, score_to_add

    def __check_snake_collisions(self):
        """
        Checks the following collisions: 
          * Snake with Apples - Adds points to the user
          * Snake with Snake  - Ends the game due to a loss
          * Snake with bomb   - Ends the game due to a loss (draw only the bomb)
          * Snake with border - Ends the game due to a loss

        This function returns the current game state (keep playing, win or lose) and
        the amount of points the user should be granted by the end of the tick
        """

        # Checks if the snake collided with itself
        collision_with_self = False
        collision_with_border = False
        collision_with_bomb = False

        # Checks collision of the snake with border/snake (next snake position)
        snake_nodes = self.__snake.draw()
        bomb_cords = self.__bomb.draw()

        for i in range(len(snake_nodes)):
            # Checks snake collision with border
            if not self.__is_cord_in_bounds(snake_nodes[i]):
                collision_with_border = True

            # Checks snake collision with bomb
            for bomb_cord in bomb_cords:
                if snake_nodes[i][0] == bomb_cord[0] and \
                        snake_nodes[i][1] == bomb_cord[1]:
                    collision_with_bomb = True

            # Checks snake collision with self
            for j in range(i + 1, len(snake_nodes)):
                if snake_nodes[i][0] == snake_nodes[j][0] and \
                        snake_nodes[i][1] == snake_nodes[j][1]:
                    collision_with_self = True

        if collision_with_bomb or collision_with_border or collision_with_self:
            return (LOSE, 0)
        

        added_score = 0
        eaten_apples = []

        # Checks snake collision with apples
        for snake_node in self.__snake.draw():
            for apple in self.__apples:
                if apple.get_cord()[0] == snake_node[0] and \
                        apple.get_cord()[1] == snake_node[1]:
                    eaten_apples.append(apple)  

        # Replaces eaten apples, updates snake & score
        for apple in eaten_apples:
            self.__snake.add_length(SNAKE_GROWTH_FOR_APPLE)
            self.__apples.remove(apple)
            added_score += apple.get_score()

        # Adds the missing apples
        if not self.__add_apples():
            return (WIN, added_score)
        
        return (KEEP_PLAYING, added_score)

    def __check_bomb_collisions(self):
        """
        Checks the following collisions: 
          * Bomb/Blast with Snake  - Ends the game due to a lose (draw only the bomb)
          * Bomb/Blast with Apples - Removes the damaged apples and adds new ones (same round!)
          * Bomb/Blast with Border - Replaces the bomb with a new one

        This function returns the current game state (keep playing, win or lose) and
        the amount of points the user should be granted by the end of the tick
        """

        collision_with_snake = False

        snake_nodes = self.__snake.draw()
        bomb_cords = self.__bomb.draw()

        # Loops over all bomb cords & snake cords. If there's an overlapping cord
        # it means the snake was hit - collision with snake is set to True
        for bomb_cord in bomb_cords:
            for snake_node in snake_nodes:
                if snake_node[0] == bomb_cord[0] and \
                        snake_node[1] == bomb_cord[1]:
                    collision_with_snake = True
        
        if collision_with_snake:
            return (LOSE, 0)


        hit_apples = []

        # Loops over all apples and removes the apples that were hit by the bomb
        for bomb_cell in self.__bomb.draw():
            for apple in self.__apples:
                if apple.get_cord()[0] == bomb_cell[0] and \
                        apple.get_cord()[1] == bomb_cell[1]:
                    hit_apples.append(apple)

        for apple in hit_apples:
            self.__apples.remove(apple)
        

        # Loops over all bomb cells. If there's a cell outside of the bounds
        # we want to replace the bomb with a new one
        for cell in self.__bomb.draw():
            if not self.__is_cord_in_bounds(cell):
                self.__add_bomb()
                break

            
        # Adds the missing apples
        if not self.__add_apples():
            return (WIN, 0)

        return (KEEP_PLAYING, 0)

    def draw(self):
        """
        Returns a list of all cells to draw in the following format:
        (X, Y, Color)

        If the bomb is outside of the border, we also want to re-set it
        with a new bomb
        """

        pixels: list[tuple[int, int, str]] = []

        # Adding all apple pixel to the list of pixel
        for apple in self.__apples:
            for cell in apple.draw():
                pixels.append(cell)
        
        # Adding all bomb pixels to the list of pixels
        pixels += self.__bomb.draw()

        # Adding all snake cells that aren't hit by the bomb/blast to the list of pixels
        for cell in self.__snake.draw():
            if self.__is_cord_in_bounds(cell):
                if not self.__is_cord_in_list(cell, self.__bomb.draw()):
                    pixels.append(cell)

        return pixels


    def __is_cord_in_list(self, cord, list_of_cords):
        """
        A util function to check if the given cord is inside the give list of cords
        """

        for cord_in_list in list_of_cords:
            if cord_in_list[0] == cord[0] and cord_in_list[1] == cord[1]:
                return True

        return False

    def __is_cord_in_bounds(self, cord):
        """
        A util function to check if the given cord is within bounds
        """

        if cord[0] < 0 or cord[0] >= self.__width:
            return False
        if cord[1] < 0 or cord[1] >= self.__height:
            return False
        
        return True

    def __is_cord_empty(self, cord):
        """
        A util function to check if the given cord is empty
        """

        for apple in self.__apples:
            if cord[0] == apple.draw()[0] and cord[1] == apple.draw()[1]:
                return False
        
        for bomb_cord in self.__bomb.draw():
            if cord[0] == bomb_cord[0] and cord[1] == bomb_cord[1]:
                return False
        
        for snake_node in self.__snake.draw():
            if cord[0] == snake_node[0] and cord[1] == snake_node[1]:
                return False
        
        return True


    def set_data(self, apples, bomb):
        self.__apples = apples
        self.__bomb = bomb

    def print_data(self):
        print("apples", self.__apples)
        print("bomb", self.__bomb)