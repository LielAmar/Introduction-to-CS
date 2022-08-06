class Direction:

    def __init__(self, x_diff: int, y_diff: int):
        self.__x_diff = x_diff
        self.__y_diff = y_diff

        self.__allowed_switches: list = []

    def add_allowed_switch(self, direction):
        self.__allowed_switches.append(direction)

    def is_allowed_switch(self, direction):
        return direction in self.__allowed_switches

    def get_diff(self):
        return (self.__x_diff, self.__y_diff)
