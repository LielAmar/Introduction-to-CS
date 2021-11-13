# import PIL
import ex5_helper

def separate_channels(image):
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

def combine_channels(channels):
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


def RGB2grayscale(colored_image):
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

            updated_value = int(round(column[0] * 0.299 + column[1] * 0.587 + column[2] * 0.114))
            grayed_image[row_index][column_index] = updated_value

    return grayed_image


def blur_kernel(size):
    """
    Creates a kernel blur array of size
    """

    kernel_array = [[] for i in range(size)]

    for row_index in range(len(kernel_array)):
        value = 1/(size**2)

        kernel_array[row_index] = [value for i in range(size)]

    return kernel_array

def apply_kernel(image, kernel):
    """
    Applies the Kernel Box Blur to the given image in ${image}
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

            updated_pixel_value = int(round(updated_pixel_value))
            updated_pixel_value = max(0, updated_pixel_value)
            updated_pixel_value = min(255, updated_pixel_value)
            
            new_image[row_index][column_index] = updated_pixel_value

    return new_image



if __name__ == "__main__":
    img = ex5_helper.load_image("examples/girl.jpg")
    separated = separate_channels(img)
    
    ex5_helper.show_image(img)
    blured = apply_kernel(separated[0], blur_kernel(3))
    # grayed = RGB2grayscale(img)

    ex5_helper.show_image(blured)