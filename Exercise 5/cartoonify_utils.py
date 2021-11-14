def check_within(x: int, y: int, min_x: int, min_y: int, max_x: int, max_y: int) -> bool:
    return x >= min_x and x < max_x and y >= min_y and y < max_y


class Pixel:
    def __init__(self, y: int, x: int, value: int):
        self.y = y
        self.x = x
        self.value = value
    
    def is_outside_border(self, max_y: int, max_x: int) -> bool:
        return not check_within(self.x, self.y, 0, 0, max_x, max_y)