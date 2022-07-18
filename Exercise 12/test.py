from ex12_utils import *


def test_is_valid_path1():
    board = [['F', 'N', 'B', 'T'],
             ['X', 'Y', 'L', 'T'],
             ['Y', 'C', 'W', 'H'],
             ['O', 'A', 'E', 'R']]
    words = ["TBL", "FXY", "YCWA", "AWE"]
    assert is_valid_path(board, [(0, 3), (0, 2), (1, 2)], words)
    assert is_valid_path(board, [(0, 0), (1, 0), (2, 0)], words)
    assert is_valid_path(board, [(2, 0), (2, 1), (2, 2), (3, 1)], words)
    assert is_valid_path(board, [(3, 1), (2, 2), (3, 2)], words)
    assert not is_valid_path(board, [(0, 0), (1, 1)], words)

def test_is_valid_path2():
    words = ["HELLO", "LIEL", "DANIEL", "ABC", "DOG"]
    board = [
            ["H", "D", "A", "B"],
            ["E", "L", "N", "C"],
            ["L", "O", "I", "E"],
            ["D", "O", "G", "L"]
        ]
    
    assert is_valid_path(board, [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1)], words) == "HELLO"

def test_is_valid_path3():
    words = read_file("boggle_dict.txt")

    board = [
            ["V", "M", "D", "Y"],
            ["S", "S", "B", "QU"],
            ["D", "O", "Z", "T"],
            ["H", "G", "O", "T"]
        ]
    
    assert is_valid_path(board, [(2, 0), (2, 1), (3, 1)], words) == "DOG"

test_is_valid_path3()
def test_find_length_n_paths():
    n = 3
    words = ["ABC", "ADG", "AEI", "AEF", "ADH", "AGH"]
    board = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]

    result = find_length_n_paths(n, board, words)
    result.sort()

    for path in result:
        assert is_valid_path(board, path, words) in words

def test_find_length_n_paths_2():
    n = 3
    words = ["ABO", "AEHI", "AEI", "AEQU", "ABOC", "CFE"]
    board = [
        ['A', 'BO', 'C'],
        ['EH', 'E', 'F'],
        ['I', 'H', 'QU']
    ]

    result = find_length_n_paths(n, board, words)
    result.sort()

    for path in result:
        assert is_valid_path(board, path, words) in words

def test_find_length_n_words():
    words = ["ABC", "AD", "AEQU", "AE", "ADH", "AG", "EQU", "QU"]
    board = [
        ['A', 'B', 'Q'],
        ['D', 'E', 'U'],
        ['G', 'H', 'QU']
    ]

    result = find_length_n_words(2, board, words)
    result.sort()
    assert result == [[(0, 0), (1, 0)], [(0, 0), (1, 1)],
                      [(0, 2), (1, 2)], [(2, 2)]]

    result = find_length_n_words(3, board, words)
    result.sort()
    assert result == [[(0, 0), (1, 0), (2, 1)], [
        (1, 1), (0, 2), (1, 2)], [(1, 1), (2, 2)]]


def test_max_score_paths():
    words = ['ABC', 'AD', 'ADH', 'AE', 'AEQU', 'AG', 'EQU', 'QU']
    board = [
        ['A', 'B', 'Q'],
        ['D', 'E', 'U'],
        ['G', 'H', 'QU']
    ]
    result = max_score_paths(board, words)
    result.sort()
    assert result == [[(0, 0), (1, 0)],
                      [(0, 0), (1, 0), (2, 1)],
                      [(0, 0), (1, 1)],
                      [(0, 0), (1, 1), (0, 2), (1, 2)],
                      [(0, 2), (1, 2)],
                      [(1, 1), (0, 2), (1, 2)]]

def test_2():
    is_valid_path([['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'G', 'K', 'L'], ['M', 'N', 'O', 'P']],[(0, 0), (0, 1), (0, 2)], ('ABC', 'CDE', 'ABCD'))