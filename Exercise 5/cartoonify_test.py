from cartoonify import *
# from test_ex5 import *

def test_separate_channels_functions():
    assert separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    
    # Custom Tests
    assert separate_channels([[[1, 2], [1, 2]]]) == [[[1, 1]], [[2, 2]]]
    assert separate_channels([[[1, 2]], [[1, 2]]]) == [[[1], [1]], [[2], [2]]]

def test_combine_channels_function():
    assert combine_channels([[[1]], [[2]]]) == [[[1, 2]]]

    # Custom Tests
    assert combine_channels([[[1, 1]], [[2, 2]]]) == [[[1, 2], [1, 2]]]
    assert combine_channels([[[1], [1]], [[2], [2]]]) == [[[1, 2]], [[1,2]]]


def test_rgb_grayscale_function():
    assert RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert RGB2grayscale([[[255, 20, 47]]]) == [[93]]


def test_blur_kernel_function():
    assert blur_kernel(3) == [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
    assert blur_kernel(5) == [
        [1/25, 1/25, 1/25, 1/25, 1/25],
        [1/25, 1/25, 1/25, 1/25, 1/25],
        [1/25, 1/25, 1/25, 1/25, 1/25],
        [1/25, 1/25, 1/25, 1/25, 1/25],
        [1/25, 1/25, 1/25, 1/25, 1/25]
    ]

def test_apply_kernel_function():
    assert apply_kernel([[0, 128, 255]], blur_kernel(3))
    assert apply_kernel([[300,300,300]], blur_kernel(3)) == [[255, 255, 255]]
    assert apply_kernel([[5,-20,-5]], blur_kernel(3)) == [[2, 0, 0]]

def test_bilinear_interpolation_function():
    assert bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0
    assert bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160

def test_resize_function():
    assert resize([[0, 64], [128, 255]], 3, 3) == [[0, 32, 64], [64, 112, 160], [128, 192, 255]]

def test_rotate_90_function():
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]]
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]]

# example3 = [[67, 94, 122, 96, 70],
#             [104, 109, 114, 102, 89],]
# result3 = [[0, 0, 255, 255, 0],
#             [255, 255, 255, 255, 255],
#             [255, 255, 0, 255, 255],
#             [255, 255, 0, 255, 255],
#             [255, 255, 0, 255, 255]]

# print(get_edges(example3, 1, 3, 5))
# print(get_edges(example3, 1, 3, 5) == result3)



def test_get_edges_function():
    assert get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]]

def test_quantize_function():
    assert quantize([[0, 50, 100], [150, 200, 250]], 8) == [[0, 32, 96], [128, 191, 223]]

def test_add_mask_function():
    assert add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]) == [[200, 125, 50]]
    
# example1 = [[0, 64], [128, 255]]
# in_margin(bilinear_interpolation(example1, 0.5, 0.5), 112)

# example2 = [[67, 122, 70], [214, 89, 147]]
# print(bilinear_interpolation(example2, 1.3, 0.8))


# print(rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]])
# print(rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]])

# bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
# bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
# bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160




# combine_channels([[[1], [1]], [[2], [2]]]) == [[[1, 2]], [[1,2]]]
# separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
# blur_kernel(3) == [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]