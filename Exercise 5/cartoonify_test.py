from cartoonify import *

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

# bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
# bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
# bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160



# combine_channels([[[1], [1]], [[2], [2]]]) == [[[1, 2]], [[1,2]]]
# separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
# blur_kernel(3) == [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]