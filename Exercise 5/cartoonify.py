# import PIL
import math

import ex5_helper

def separate_channels(image: list) -> list:
    """
    Breaks down the a 3d array into a list of 2d arrays

    Example: [[[1, 2]]] -> [[[1]], [[2]]]
    """

    # Creates a sub-list for every channel
    amnt_of_chnls = len(image[0][0])
    separated = [[] for i in range(amnt_of_chnls)]

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
    combined = [[[] for j in range(amnt_of_clmns)] for i in range(amnt_of_rows)]

    # Loops over all rows in ${channels} and appends X arrays for each column of each row in ${channels}
    # Then it loops over all channels and appends that value to the appropriate column in ${combined}
    for row_index in range(amnt_of_rows):
        # for column_index in range(amnt_of_clmns):
            # combined[row_index].append([])

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

    grayed_image = [[[] for j in range(amnt_of_clmns)] for i in range(amnt_of_rows)]

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

    kernel_array = [[] for i in range(size)]

    for row_index in range(len(kernel_array)):
        value = 1/(size**2)

        kernel_array[row_index] = [value for i in range(size)]

    return kernel_array

def apply_kernel(image: list, kernel: list) -> list:
    """
    Applies the Kernel Box Blur to the given image in ${image}
    The image is represented by a single channel as a 2d array
    """

    kernel_size = len(kernel)

    new_image = [[0 for j in range(len(image[0]))] for i in range(len(image))]

    for row_index in range(len(new_image)):
        for column_index in range(len(image[row_index])):
            updated_pixel_value = 0

            for i in range(0-int((kernel_size/2)), 0 + int((kernel_size/2)+1)):
                for j in range(0-int((kernel_size/2)), 0 + int((kernel_size/2)+1)):
                    kernel_value = kernel[i+1][j+1]

                    pixel_row = row_index + i
                    pixel_column = column_index + j

                    # If the checked pixel is outside the image's border, set it to the central pixel
                    if (pixel_row < 0 or pixel_row >= len(image)
                            or pixel_column < 0 or pixel_column >= len(image[row_index])):
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

    y_axis_perc = y - math.floor(y)
    x_axis_perc = x - math.floor(x)


    # Getting the indexes of all 4 nearby pixels
    nearby_pixels = {
        "top_left": (math.floor(y), math.floor(x)),      # 0, 0
        "bot_left": (math.floor(y+1), math.floor(x)),    # 1, 0
        "top_right": (math.floor(y), math.floor(x+1)),   # 0, 1
        "bot_right": (math.floor(y+1), math.floor(x+1))  # 1, 1
    }
    
    # Looping over all nearby pixel. If a pixel is outside the image borders
    # we want to set its calculated value to 0 so it doesn't affect the final
    # calculation of the updated pixel value
    for key, pixel in nearby_pixels.items():
        # print("pixel: " + str(pixel))

        if (pixel[0] < 0 or pixel[0] >= len(image)
                or pixel[1] < 0 or pixel[1] >= len(image[y_rounded])):
            # Pixel is outside the image's border
            nearby_pixels[key] = image[y_rounded][x_rounded]
        else:
            # Pixel is inside the image's border
            nearby_pixels[key] = image[pixel[0]][pixel[1]]

    print("nearby_pixels: " + str(nearby_pixels))

    updated_pixel_value = 0

    # if nearby_pixels["top_left"] != -1:
    #     updated_pixel_value += nearby_pixels["top_left"] * (1 - x_axis_perc) * (1 - y_axis_perc)
    # if nearby_pixels["bot_left"] != -1:
    #     updated_pixel_value += nearby_pixels["bot_left"] * y_axis_perc * (1 - x_axis_perc)
    # if nearby_pixels["top_right"] != -1:
    #     updated_pixel_value += nearby_pixels["top_right"] * x_axis_perc * (1 - y_axis_perc)
    # if nearby_pixels["bot_right"] != -1:
    #     updated_pixel_value += nearby_pixels["bot_right"] * x_axis_perc * y_axis_perc

    # Calculating the pixel's new value
    updated_pixel_value = (
    max(0, min(
              nearby_pixels["top_left"]  * (1 - x_axis_perc) * (1 - y_axis_perc)
            + nearby_pixels["bot_left"]  * y_axis_perc * (1 - x_axis_perc)
            + nearby_pixels["top_right"] * x_axis_perc * (1 - y_axis_perc)
            + nearby_pixels["bot_right"] * x_axis_perc * y_axis_perc
    , 255))
    )
    updated_pixel_value = round(updated_pixel_value)

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
        
        for column_index in range(new_width):
            # relative_y_val = ((0.5 + row_index) / new_width) * amnt_of_rows
            # relative_x_val = ((0.5 + column_index) / new_height) * amnt_of_columns
            # relative_y_val = (row_index * amnt_of_rows) / new_width
            # relative_x_val = (column_index * amnt_of_columns) / new_height
            relative_y_val = ((row_index) / new_width) * amnt_of_rows
            relative_x_val = ((column_index) / new_height) * amnt_of_columns

            updated_pixel_value = bilinear_interpolation(image, relative_y_val, relative_x_val)
            updated_row.append(updated_pixel_value)
            
            # updated_row.append(updated_column)

        # updated_row
        updated_image.append(updated_row)

    return updated_image


def rotate_90(image: list, direction: str) -> list:
    # [[1, 2, 3], [4, 5, 6]]
    # [[(1, 2)]]
    amnt_of_rows = len(image)
    amnt_of_columns = len(image[0])

    rotated = [[] for i in range(amnt_of_columns)]

    if direction == "R":
        for row_index in range(len(image) - 1, -1, -1):
            for column_index in range(0, len(image[row_index])):
                rotated[column_index].append(image[row_index][column_index])
                
    elif direction == "L":
        for row_index in range(0, len(image)):
            for column_index in range(len(image[row_index]) - 1, -1, -1):
                rotated[len(image[row_index]) - 1 - column_index].append(image[row_index][column_index])

    return rotated




if __name__ == "__main__":
    img = ex5_helper.load_image("examples/girl.jpg")
    separated = separate_channels(img)
    
    # ex5_helper.show_image(img)
    # blured = apply_kernel(separated[0], blur_kernel(3))
    # grayed = RGB2grayscale(img)
    # separated[0] = resize(separated[0], 8, 8)
    # separated[1] = resize(separated[1], 8, 8)
    # separated[2] = resize(separated[2], 8, 8)

    # combined = combine_channels(separated)

    # ex5_helper.show_image(combined)
    # ex5_helper.show_image(separated[0])
    
    img = rotate_90(img, "L")
    ex5_helper.show_image(img)
    