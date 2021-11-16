'''⸮⁉'''
import difflib
import pprint
import unittest
import urllib.request
from typing import Any

import cartoonify as user


class CartoonifyTests(unittest.TestCase):
    MAX_DIFF_ALLOWED = 1
    EXPECTED_CHANGED_MSG = "You've changed the input matrix, which according to the PDF is ont allowed"
    BETA_TEST_WARNING = '''
    #######################
    # THIS IS A BETA TEST #
    #######################
    '''

    def test__separate_channels__example_form_pdf(self):
        self.assertListEqual(
            [[[1]], [[2]]],
            user.separate_channels([[[1, 2]]]),
            'Example given on page 2'
        )

    def test__separate_channels__example_from_forum(self):
        self.assertListEqual(
            [[[1, 4], [7, 10]],
             [[2, 5], [8, 11]],
             [[3, 6], [9, 12]]],
            user.separate_channels(
                [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
            ),
            'Example from the forum: https://moodle2.cs.huji.ac.il/nu21/mod/forumng/discuss.php?d=2226&expand=1#p5642'
        )

    def test__separate_channels__more_examples(self):
        self.assertListEqual(
            [[[170, 45, 175], [251, 74, 79]],
             [[20, 154, 28], [210, 105, 183]],
             [[35, 161, 9], [134, 46, 139]]],
            user.separate_channels(
                [
                    [[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                    [[251, 210, 134], [74, 105, 46], [79, 183, 139]]
                ]
            )
        )

    def test__combine_channels__example_from_pdf(self):
        input_ = [[[1]], [[2]]]
        self.assertListEqual(
            [[[1, 2]]],
            user.combine_channels(input_),
            'Example given on page 2'
        )

    def test__combine_channels__example_from_forum(self):
        self.assertListEqual(
            [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
            user.combine_channels(
                [[[1, 4], [7, 10]],
                 [[2, 5], [8, 11]],
                 [[3, 6], [9, 12]]]),
            'Example from the forum: https://moodle2.cs.huji.ac.il/nu21/mod/forumng/discuss.php?d=2226&expand=1#p5642'
        )

    def test__combine_channels__more_examples(self):
        self.assertListEqual(
            [
                [[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]
            ],
            user.combine_channels(
                [[[170, 45, 175], [251, 74, 79]],
                 [[20, 154, 28], [210, 105, 183]],
                    [[35, 161, 9], [134, 46, 139]]]
            )
        )

    def test__RGB2grayscale__example_from_pdf(self):
        input_ = [[[100, 180, 240]]]
        self.assertListEqual(
            [[163]],
            user.RGB2grayscale(input_),
            'Example given on page 3'
        )

    def test__RGB2grayscale__more_examples(self):
        self.assertListAlmostEqual(
            a1=[[67, 122, 70], [214, 89, 147]],
            a2=user.RGB2grayscale(
                [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                 [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
            ),
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__blur_kernel__example_from_pdf(self):
        self.assertListEqual(
            [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],
            user.blur_kernel(3),
            'Example given on page 3'
        )

    def test__blur_kernel__other_values(self):
        self.assertListEqual(
            [[1 / 25 for _ in range(5)] for _ in range(5)],
            user.blur_kernel(5),
            'Kernel size of 5'
        )
        self.assertListEqual(
            [[1 / 49 for _ in range(7)] for _ in range(7)],
            user.blur_kernel(7),
            'Kernel size of 7'
        )

    def test__apply_kernel__example_from_pdf(self):
        blur_kernel = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
        self.assertListEqual(
            [[14, 128, 241]],
            user.apply_kernel([[0, 128, 255]], blur_kernel),
            'Example given on page 3'
        )

    def test__apply_kernel__more_examples(self):
        blur_kernel = [[0.04, 0.04, 0.04, 0.04, 0.04],
                       [0.04, 0.04, 0.04, 0.04, 0.04],
                       [0.04, 0.04, 0.04, 0.04, 0.04],
                       [0.04, 0.04, 0.04, 0.04, 0.04],
                       [0.04, 0.04, 0.04, 0.04, 0.04]]
        self.assertListEqual(
            [[79, 121, 82], [191, 96, 140]],
            user.apply_kernel([[67, 122, 70], [214, 89, 147]], blur_kernel),
            CartoonifyTests.BETA_TEST_WARNING
        )

    def test__apply_kernel__supports_generic_kernel(self):
        kernel = [[0.01, 0.02, 0.03], [0.04, 0.05, 0.06], [0.07, 0.08, 0.09]]
        self.assertListAlmostEqual(
            [[47, 56, 41], [83, 48, 62]],
            user.apply_kernel(
                [[67, 122, 70], [214, 89, 147]], 
                kernel
            ),
            delta=CartoonifyTests.MAX_DIFF_ALLOWED,
            msg=CartoonifyTests.BETA_TEST_WARNING +
            '\nAccording to https://moodle2.cs.huji.ac.il/nu21/mod/forumng/discuss.php?d=2288#p6063, apply_kernel should support any kernel'
        )

    def test__bilinear_interpolation__example_from_pdf(self):
        image = [[0, 64], [128, 255]]
        self.assertAlmostEqual(
            0,
            user.bilinear_interpolation(image, 0, 0),
            msg='Example 1 of 4 given on page 4',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )
        self.assertAlmostEqual(
            255,
            user.bilinear_interpolation(image, 1, 1),
            msg='Example 2 of 4 given on page 4',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )
        self.assertAlmostEqual(
            112,
            user.bilinear_interpolation(image, 0.5, 0.5),
            msg='Example 3 of 4 given on page 4',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )
        self.assertAlmostEqual(
            160,
            user.bilinear_interpolation(image, 0.5, 1),
            msg='Example 4 of 4 given on page 4',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__bilinear_interpolation__more_tests_on_3by3(self):
        image = [[67, 122, 70], [214, 89, 147]]
        self.assertAlmostEqual(
            114,
            user.bilinear_interpolation(image, 1.3, 0.8),
            msg='NAME ME',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__bilinear_interpolation__example_from_forum(self):
        self.assertAlmostEqual(
            4,
            user.bilinear_interpolation(
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0.5, 1.25),
            msg='Based on the images posted by TA Adi Ravid',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__rotate_90__example_from_pdf(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertListEqual(
            [[4, 1], [5, 2], [6, 3]],
            user.rotate_90(matrix, 'R'),
            'Example 1/2 given on page 5'
        )
        self.assertListEqual(
            [[3, 6], [2, 5], [1, 4]],
            user.rotate_90(matrix, 'L'),
            'Example 2/2 given on page 5'
        )

    def test__rotate_90__more_examples(self):
        matrix = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                  [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
        self.assertListEqual(
            [[[251, 210, 134], [170, 20, 35]],
             [[74, 105, 46], [45, 154, 161]],
             [[79, 183, 139], [175, 28, 9]]],
            user.rotate_90(matrix, 'R')
        )
        self.assertListEqual(
            [[[175, 28, 9], [79, 183, 139]],
             [[45, 154, 161], [74, 105, 46]],
             [[170, 20, 35], [251, 210, 134]]],
            user.rotate_90(matrix, 'L')
        )

    def test__get_edges__example_from_pdf(self):
        self.assertListEqual(
            [[255, 0, 255]],
            user.get_edges([[200, 50, 200]], 3, 3, 10),
            'Example given on page 6'
        )

    def test__get_edges__more_examples(self):
        self.assertListEqual(
            [[0, 255, 0], [255, 255, 255]],
            user.get_edges([[67, 122, 70], [214, 89, 147]], 3, 5, 5)
        )
        self.assertListEqual(
            [[0, 0, 255, 255, 0],
             [255, 255, 255, 255, 255],
             [255, 255, 0, 255, 255],
             [255, 255, 0, 255, 255],
             [255, 255, 0, 255, 255]],
            user.get_edges(
                [[67, 94, 122, 96, 70],
                 [104, 109, 114, 102, 89],
                 [140, 123, 106, 107, 108],
                 [177, 137, 97, 112, 128],
                 [214, 152, 89, 118, 147]], 1, 3, 5)
        )

    def test__quantize__example_from_pdf(self):
        self.assertListAlmostEqual(
            [[0, 32, 96], [128, 191, 223]],
            user.quantize([[0, 50, 100], [150, 200, 250]], 8),
            msg='Example given on page 7',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__quantize__example_from_pdf(self):
        self.assertListAlmostEqual(
            [[66, 120, 69], [212, 87, 145]],
            user.quantize([[67, 122, 70], [214, 89, 147]], 100),
            msg='Example given on page 7',
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__quantize_colored_image__various_tests(self):
        self.assertListAlmostEqual(
            [[[159, 0, 32], [32, 128, 159], [159, 0, 0]],
                [[223, 191, 128], [64, 96, 32], [64, 159, 128]]],
            user.quantize_colored_image(
                [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                 [[251, 210, 134], [74, 105, 46], [79, 183, 139]]],
                8
            ),
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )
        self.assertListAlmostEqual(
            [[[0, 8], [0, 20], [0, 28], [4, 40]],
               [[4, 48], [4, 60], [4, 68], [8, 80]],
               [[8, 88], [8, 100], [8, 108], [12, 120]],
               [[12, 128], [12, 139], [12, 147], [16, 159]]],
            user.quantize_colored_image(
               [[[1, 10], [2, 20], [3, 30], [4, 40]],
                [[5, 50], [6, 60], [7, 70], [8, 80]],
                [[9, 90], [10, 100], [11, 110], [12, 120]],
                [[13, 130], [14, 140], [15, 150], [16, 160]]], 64
            ),
            CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def test__add_mask__example_from_pdf(self):
        self.assertListEqual(
            [[200, 125, 50]],
            user.add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]),
            'Example given on page 8'
        )

    def test__add_mask__accepts_colored_image(self):
        message = '''The instructions state that `add_mask` should be able to apply
            a mask both single-channel (2d matrix) images and on multi-channel
            (3d matrix) images (by separating the colored image to channels
            and applying the mask)
            Inspired by the example on page 9'''
        self.assertListEqual(
            [[[200, 200, 200], [125, 125, 125], [50, 50, 50]]],
            user.add_mask(
                [[[50, 50, 50], [50, 50, 50], [50, 50, 50]]],
                [[[200, 200, 200], [200, 200, 200], [200, 200, 200]]],
                [[0, 0.5, 1]]
            ),
            message
        )
        self.assertListEqual(
            [[[170, 20, 35], [24, 87, 82], [60, 29, 9]],
             [[66, 82, 46], [19, 61, 29], [18, 81, 54]]],
            user.add_mask(
                [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                 [[251, 210, 134], [74, 105, 46], [79, 183, 139]]],
                [[[1, 10, 1], [2, 20, 4], [3, 30, 9]],
                 [[4, 40, 16], [5, 50, 25], [6, 60, 36]]],
                [[1.0, 0.5, 0.33], [0.25, 0.2, 0.17]]
            ),
            message
        )

    def test__cartoonify__generic_test(self):
        self.assertListAlmostEqual(
            [[[0, 0, 0], [32, 128, 159], [0, 0, 0]],
             [[223, 191, 128], [0, 0, 0], [64, 159, 128]]],
            user.cartoonify(
                [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                 [[251, 210, 134], [74, 105, 46], [79, 183, 139]]],
                3, 3, 1, 8
            ),
            delta=CartoonifyTests.MAX_DIFF_ALLOWED
        )

    def assertListAlmostEqual(self, a1, a2, delta=1, msg=None):
        msg = msg if msg else ''
        diffMsg = '\n' + '\n'.join(
            difflib.ndiff(pprint.pformat(a1).splitlines(),
                          pprint.pformat(a2).splitlines()))
        self.assertTrue(
            CartoonifyTests._are_almost_equal(
                a1,
                a2,
                -1,
                delta
            ),
            msg + '\nExpected then actual\n' + diffMsg
        )

    @staticmethod
    def _are_almost_equal(o1: Any, o2: Any, max_abs_ratio_diff: float, max_abs_diff: float) -> bool:
        """
        Compares two objects by recursively walking them trough. Equality is as usual except for floats.
        Floats are compared according to the two measures defined below.

        :param o1: The first object.
        :param o2: The second object.
        :param max_abs_ratio_diff: The maximum allowed absolute value of the difference.
        `abs(1 - (o1 / o2)` and vice-versa if o2 == 0.0. Ignored if < 0.
        :param max_abs_diff: The maximum allowed absolute difference `abs(o1 - o2)`. Ignored if < 0.
        :return: Whether the two objects are almost equal.

        https://stackoverflow.com/questions/12136762/assertalmostequal-in-python-unit-test-for-collections-of-floats
        """
        if type(o1) != type(o2):
            return False

        composite_type_passed = False

        if hasattr(o1, '__slots__'):
            if len(o1.__slots__) != len(o2.__slots__):
                return False
            if any(not CartoonifyTests._are_almost_equal(getattr(o1, s1), getattr(o2, s2),
                                                         max_abs_ratio_diff, max_abs_diff)
                   for s1, s2 in zip(sorted(o1.__slots__), sorted(o2.__slots__))):
                return False
            else:
                composite_type_passed = True

        if hasattr(o1, '__dict__'):
            if len(o1.__dict__) != len(o2.__dict__):
                return False
            if any(not CartoonifyTests._are_almost_equal(k1, k2, max_abs_ratio_diff, max_abs_diff)
                   or not CartoonifyTests._are_almost_equal(v1, v2, max_abs_ratio_diff, max_abs_diff)
                   for ((k1, v1), (k2, v2))
                   in zip(sorted(o1.__dict__.items()), sorted(o2.__dict__.items()))
                   if not k1.startswith('__')):  # avoid infinite loops
                return False
            else:
                composite_type_passed = True

        if isinstance(o1, dict):
            if len(o1) != len(o2):
                return False
            if any(not CartoonifyTests._are_almost_equal(k1, k2, max_abs_ratio_diff, max_abs_diff)
                   or not CartoonifyTests._are_almost_equal(v1, v2, max_abs_ratio_diff, max_abs_diff)
                   for ((k1, v1), (k2, v2)) in zip(sorted(o1.items()), sorted(o2.items()))):
                return False

        elif any(issubclass(o1.__class__, c) for c in (list, tuple, set)):
            if len(o1) != len(o2):
                return False
            if any(not CartoonifyTests._are_almost_equal(v1, v2, max_abs_ratio_diff, max_abs_diff)
                   for v1, v2 in zip(o1, o2)):
                return False

        elif isinstance(o1, (float)):
            if o1 == o2:
                return True
            else:
                if max_abs_ratio_diff > 0:  # if max_abs_ratio_diff < 0, max_abs_ratio_diff is ignored
                    if o2 != 0:
                        if abs(1.0 - (o1 / o2)) > max_abs_ratio_diff:
                            return False
                    else:  # if both == 0, we already returned True
                        if abs(1.0 - (o2 / o1)) > max_abs_ratio_diff:
                            return False
                # if max_abs_diff < 0, max_abs_diff is ignored
                if 0 < max_abs_diff < abs(o1 - o2):
                    return False
                return True

        else:
            if not composite_type_passed:
                return o1 == o2

        return True


def version_check():
    up_to_date = True
    req = urllib.request.Request(
        url=VERSION_CHECK, method='GET'
    )
    try:
        with urllib.request.urlopen(req) as resp:
            version = resp.read().decode(
                resp.headers.get_content_charset("utf-8")
            )
        up_to_date = int(version) <= VERSION
    except:
        print('Could not check for updates')
        up_to_date = True
    return up_to_date


def main():
    if version_check():
        print('Up to date, running tests...')
        print("If a test has failed when it shouldn't have, please contact me at yutkin@cs.huji.ac.il or open an issue or a pull request here: https://github.com/TwoUnderscorez/huji_intro2cs1_ex5")
        unittest.main()
    else:
        print("We've updated the tests file, please download the new one form here")
        print('https://raw.githubusercontent.com/TwoUnderscorez/huji_intro2cs1_ex5/master/ex5tests.py')


# .data
VERSION = 1
VERSION_CHECK = 'https://raw.githubusercontent.com/TwoUnderscorez/huji_intro2cs1_ex5/master/VERSION'

if __name__ == '__main__':
    main()
