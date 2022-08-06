class BoardObject:
    """
    A super class for all objects of the board
    It has the base properties:
    x, y, color
    """

    def __init__(self, x: int, y: int, color: str):
        self.__x = x 
        self.__y = y

        self.__color = color

    def get_cord(self):
        return (self.__x, self.__y)

    def set_cords(self, cords):
        self.__x = cords[0]
        self.__y = cords[1]
    
    def get_color(self) -> str:
        return self.__color

    # Abstract methods
    def draw(self):
        pass

    def tick(self) -> bool:
        pass