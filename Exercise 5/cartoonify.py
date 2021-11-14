import math
import time

import ex5_helper

# === Utils ===
def check_within(x: int, y: int, min_x: int, min_y: int, max_x: int, max_y: int) -> bool:
    return x >= min_x and x < max_x and y >= min_y and y < max_y


class Pixel:
    def __init__(self, y: int, x: int, value: int):
        self.y = y
        self.x = x
        self.value = value
    
    def is_outside_border(self, max_y: int, max_x: int) -> bool:
        return not check_within(self.x, self.y, 0, 0, max_x, max_y)



def separate_channels(image: list) -> list:
    """
    Breaks down the a 3d array into a list of 2d arrays

    Example: [[[1, 2]]] -> [[[1]], [[2]]]
    """

    # Creates a sub-list for every channel
    amnt_of_chnls = len(image[0][0])

    separated: list = [[] for _ in range(amnt_of_chnls)]

    # Loops over all rows in ${image} and appends a new array for each channel in ${separated}
    # Then it loops over all columns in ${image} and appends that matching index's value to
    # the appropriate row in ${separated}
    for row_index in range(len(image)):
        for channel in separated:
            channel.append([])
        
        for column in image[row_index]:
            for channel_index in range(len(separated)):
                separated[channel_index][row_index].append(column[channel_index])

    return separated

def combine_channels(channels: list) -> list:
    """
    Combines a list of 2d arrays into a 3d array

    Example: [[[1]], [[2]]] -> [[[1, 2]]]
    """

    # Creates a sub-list for every row
    amnt_of_rows = len(channels[0])
    amnt_of_clmns = len(channels[0][0])

    combined: list = [[[] for _ in range(amnt_of_clmns)] for _ in range(amnt_of_rows)]

    # Loops over all rows in ${channels} and appends X arrays for each column of each row in ${channels}
    # Then it loops over all channels and appends that value to the appropriate column in ${combined}
    for row_index in range(amnt_of_rows):
        for channel in channels:
            for column_index in range(len(channel[row_index])):
                combined[row_index][column_index].append(channel[row_index][column_index])

    return combined


def RGB2grayscale(colored_image: list) -> list:
    """
    Grayscales an RGB image through the formula: RED * 0.299 + GREEN * 0.587 + BLUE * 0.114
    Each pixel is being set the combined value of all 3 channels
    """

    amnt_of_rows = len(colored_image)
    amnt_of_clmns = len(colored_image[0])

    grayed_image: list = [[[] for _ in range(amnt_of_clmns)] for _ in range(amnt_of_rows)]

    for row_index in range(amnt_of_rows):
        for column_index in range(amnt_of_clmns):
            column = colored_image[row_index][column_index]

            updated_value = round(column[0] * 0.299 + column[1] * 0.587 + column[2] * 0.114)
            grayed_image[row_index][column_index] = updated_value

    return grayed_image


def blur_kernel(size: int) -> list:
    """
    Creates a kernel blur array of size
    """

    kernel_array: list = [[] for _ in range(size)]

    for row_index in range(len(kernel_array)):
        value = 1 / (size ** 2)

        kernel_array[row_index] = [value for _ in range(size)]

    return kernel_array

def apply_kernel(image: list, kernel: list) -> list:
    """
    Applies the Kernel Box Blur to the given image in ${image}
    The image is represented by a single channel as a 2d array
    """

    kernel_size = len(kernel)

    new_image = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    # Loops over all rows and columns and updating the pixel's value
    # The updated value is calculated by nearby pixels in the inner double-loop.
    for row_index in range(len(new_image)):
        for column_index in range(len(image[row_index])):
            updated_pixel_value = 0

            for i in range(0 - int((kernel_size / 2)), 0 + int((kernel_size / 2) + 1)):
                for j in range(0 - int((kernel_size / 2 )), 0 + int((kernel_size / 2) + 1)):
                    kernel_value = kernel[i+1][j+1]

                    pixel_row = row_index + i
                    pixel_column = column_index + j

                    # If the checked pixel is outside the image's border, set it to the central pixel
                    if not check_within(pixel_row, pixel_column, 0, 0,
                            len(image), len(image[row_index])):
                        pixel_row = row_index
                        pixel_column = column_index

                    updated_pixel_value += (image[pixel_row][pixel_column] * kernel_value)

            updated_pixel_value = round(updated_pixel_value)
            updated_pixel_value = max(0, updated_pixel_value)
            updated_pixel_value = min(255, updated_pixel_value)
            
            new_image[row_index][column_index] = updated_pixel_value

    return new_image


def bilinear_interpolation(image: list, y: float, x: float) -> int:
    """
    Invokes the bilinear interpolation resampling method.
    Calculates a pixel's value through percentages based on how close
    the pixel is to nearby pixels
    """

    y_rounded = math.floor(y)
    x_rounded = math.floor(x)

    y_axis_perc = (y - y_rounded)
    x_axis_perc = (x - x_rounded)

    # Getting the indexes of all 4 nearby pixels
    nearby_pixels = {
        "top_left":  Pixel(y_rounded,     x_rounded,     0),
        "bot_left":  Pixel(y_rounded + 1, x_rounded,     0),
        "top_right": Pixel(y_rounded,     x_rounded + 1, 0),
        "bot_right": Pixel(y_rounded + 1, x_rounded + 1, 0)
    }

    # Looping over all nearby pixel. If a pixel is outside the image borders
    # we want to set its calculated value to 0 so it doesn't affect the final
    # calculation of the updated pixel value
    for pixel in nearby_pixels.values():
        if pixel.is_outside_border(len(image), len(image[0])):
            pixel.value = image[y_rounded][x_rounded]
        else:
            pixel.value = image[pixel.y][pixel.x]

    # Calculating the pixel's new value
    updated_pixel_value = (
              nearby_pixels["top_left"].value  * (1 - x_axis_perc) * (1 - y_axis_perc)
            + nearby_pixels["bot_left"].value  * y_axis_perc       * (1 - x_axis_perc)
            + nearby_pixels["top_right"].value * x_axis_perc       * (1 - y_axis_perc)
            + nearby_pixels["bot_right"].value * x_axis_perc       * y_axis_perc
    )

    updated_pixel_value = round(max(0, min(255, updated_pixel_value)))
    return updated_pixel_value

def resize(image: list, new_height: int, new_width: int) -> list:
    """
    Resizes the given image in ${image}, as a 2d array
    to ${new_width} x ${new_height}
    """

    updated_image = []

    amnt_of_rows = len(image)
    amnt_of_columns = len(image[0])

    for row_index in range(new_height):
        updated_row = []

        relative_y_val = ((row_index) / (new_height - 1)) * (amnt_of_rows - 1)

        for column_index in range(new_width):
            relative_x_val = ((column_index) / (new_width - 1)) * (amnt_of_columns - 1)

            updated_row.append(bilinear_interpolation(image, relative_y_val, relative_x_val))

        updated_image.append(updated_row)

    return updated_image


def rotate_90(image: list, direction: str) -> list:
    """
    Rotates the given image in ${image} by 90 degrees in ${direction}
    """

    amnt_of_columns = len(image[0])

    rotated: list = [[] for i in range(amnt_of_columns)]

    if direction == "R":
        for row_index in range(len(image) - 1, -1, -1):
            for column_index in range(0, len(image[row_index])):
                rotated[column_index].append(image[row_index][column_index])
                
    elif direction == "L":
        for row_index in range(0, len(image)):
            for column_index in range(len(image[row_index]) - 1, -1, -1):
                rotated[len(image[row_index]) - 1 - column_index].append(
                            image[row_index][column_index])

    return rotated


def get_edges(image: list, blur_size: int, block_size: int, c: int) -> list:
    """
    Applies blur of ${blur_size} to the image and then
    calculates the edges of the given image in ${image}
    """

    blurred = apply_kernel(image, blur_kernel(blur_size))

    amnt_of_rows = len(blurred)
    amnt_of_clmns = len(blurred[0])

    r = block_size // 2

    edged: list = []

    # Looping over all rows and columns.
    # For every iteration, we loop over all nearby pixels, starting from
    # (row_idx - r) to (row_idx + r + 2) and (column_idx - r) to (column_idx + r + 2)
    #   For every inner iteration we add check whether the pixel has a valid position
    #   If it does, we add to the avarage calculation, else we add the outer pixel's value
    for row_idx in range(amnt_of_rows - 1):
        row = []

        for column_idx in range(amnt_of_clmns - 1):
            avg = []

            for i in range(row_idx - r, row_idx + r + 1 + 1):
                for j in range(column_idx - r, column_idx + r + 1 + 1):

                    if check_within(i, j, 0, 0, amnt_of_rows, amnt_of_clmns):
                        avg.append(blurred[i][j])
                    else:
                        avg.append(blurred[row_idx][column_idx])

            treshold = sum(avg) / len(avg)
            row.append(0 if treshold - c > blurred[row_idx][column_idx] else 255)

        edged.append(row)

    return edged



if __name__ == "__main__":
    start = time.time()

    img = ex5_helper.load_image("examples/ziggy.jpg")
    print("got image")

    img = RGB2grayscale(img)
    print("grayed image")
    # ex5_helper.show_image(img)

    img = resize(img, 258, 460)
    print("resized image")
    # ex5_helper.show_image(img)

    img = get_edges(img, 5, 13, 11)
    print("edged image")
    ex5_helper.show_image(img)

    end = time.time()

    print("time taken: " + str(end - start))
    
    # ex5_helper.show_image(img)
    # blured = apply_kernel(separated[0], blur_kernel(3))
    # grayed = RGB2grayscale(img)
    # separated[0] = resize(separated[0], 16, 16)
    # separated[1] = resize(separated[1], 16, 16)
    # separated[2] = resize(separated[2], 16, 16)

    # combined = combine_channels(separated)

    # ex5_helper.show_image(combined)
    # ex5_helper.show_image(separated[0])

    # img = rotate_90(img, "L")
    # ex5_helper.show_image(img)
    
    # print(resize([[0,1],[2,3]],10,10))