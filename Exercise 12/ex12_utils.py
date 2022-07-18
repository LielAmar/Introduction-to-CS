from typing import Generator, Iterable, Optional, Dict, List, Tuple

from constants import *


def is_valid_path(board: List[List[str]], path: List[Tuple[int, int]], words: Iterable[str]) \
        -> Optional[str]:
    """
    Returns a word if a given path creates a word which is in the words iterable
    """

    # Type validation
    if not isinstance(board, List):
        raise TypeError("${board} must be a 2D array of strings")
    if not isinstance(path, List):
        raise TypeError("${path} must be a list of tuples representing coordinates")
    if not isinstance(words, Iterable):
        raise TypeError("${words} must be an iterable object of strings")

    if not is_legal_path(board, path):
        return None

    word = ""

    for coord in path:
        word += board[coord[ROW_INDEX]][coord[COLUMN_INDEX]]

    return word if word in words else None


def find_length_n_paths(n: int, board: List[List[str]], words: Iterable[str]) \
        -> List[List[Tuple[int, int]]]:
    """
    Returns a list of all paths of length ${n} to words in ${words}
    """

    # Type validation
    if not isinstance(n, int):
        raise TypeError("${n} must be an integer")
    if not isinstance(board, List):
        raise TypeError("${board} must be a 2D array of strings")
    if not isinstance(words, Iterable):
        raise TypeError("${words} must be an iterable object of strings")

    if n == 0: return []

    def __n_paths_helper(n, board, words, current_path):
        """
        A recursive-helper function to calculate all possible paths from the
        last coordinate in ${current_path}, that leads to a word in words
        """

        # If we don't have any word starting with crr_str we break
        # if any([True for word in words if word.startswith(crr_str)]):
        if n <= 0:
            # If we've reached an end, we want to check if the built path
            # led us to a valid word (and is valid by itself).
            # If it is we return the current_path, otherwise we return an empty list
            if is_valid_path(board, current_path, words):
                return [current_path]

            return []

        # Filtering remaining words
        crr_word = __build_word_from_path(board, current_path)
        words    = [word for word in words if word.startswith(crr_word)]
        if len(words) == 0: return []

        # Runs the bruteforce logic with __n_paths_helper as the recursion
        # function returning the valid data for it
        paths = __bruteforce_paths(board, current_path, lambda new_cord:
                __n_paths_helper(n-1, board, words, current_path + [new_cord]))

        return paths

    words = [word for word in words if len(word) >= n]

    paths = []

    # Loops over all possible starting positions and adds the possible paths
    # starting from that position
    for row, col in __board_iterator(board):
        paths += __n_paths_helper(n - 1, board, words, [(row, col)])

    return paths


def find_length_n_words(n: int, board: List[List[str]], words: Iterable[str]) \
        -> List[List[Tuple[int, int]]]:
    """
    Returns a list of all paths to words in ${words} of length ${n}
    """

    # Type validation
    if not isinstance(n, int):
        raise TypeError("${n} must be an integer")
    if not isinstance(board, List):
        raise TypeError("${board} must be a 2D array of strings")
    if not isinstance(words, Iterable):
        raise TypeError("${words} must be an iterable object of strings")

    if n == 0: return []

    def __n_words_helper(n, board, words, current_path):
        """
        A recursive-helper function to calculate all possible paths from the
        last coordinate in ${current_path}, that leads to a word in words
        """

        # Filtering remaining words
        crr_word = __build_word_from_path(board, current_path)
        words    = [word for word in words if word.startswith(crr_word)]
        if len(words) == 0: return []

        # If we've reached a dead-end (no matching word), or our word is of length
        # greather than ${n}, we want to return an empty list.
        # If our word's length is exactly n, we found a valid path and we return it.

        if len(crr_word) > n:
            return []

        if len(crr_word) == n:
            if is_valid_path(board, current_path, words):
                return [current_path]
            return []



        # Runs the bruteforce logic with __n_words_helper as the recursion
        # function returning the valid data for it
        paths = __bruteforce_paths(board, current_path, lambda new_cord:
                __n_words_helper(n, board, words, current_path + [new_cord]))

        return paths

    # Filter out all words that are not of length ${n}
    words = [word for word in words if len(word) == n]

    paths = []

    # Loops over all possible starting positions and adds the possible paths
    # starting from that position
    for row, col in __board_iterator(board):
        paths += __n_words_helper(n, board, words, [(row, col)])

    return paths


def max_score_paths(board: List[List[str]], words: Iterable[str]) \
        -> List[List[Tuple[int, int]]]:
    """
    Returns the paths that would lead to the highest score
    """

    # Type validation
    if not isinstance(board, List):
        raise TypeError("${board} must be a 2D array of strings")
    if not isinstance(words, Iterable):
        raise TypeError("${words} must be an iterable object of strings")

    
    paths_by_length = dict()
    words_by_length: Dict[int, List[str]] = dict()

    # Loops over all words and seperates them into a dictionary by length
    for word in words:
        length = len(word)

        if length not in words_by_length:
            words_by_length[length] = []

        words_by_length[length].append(word)

    # Loops over all keys in words by length and finds all possible words of length
    # ${key} given board ${board}
    for key in words_by_length.keys():
        paths_by_length[key] = find_length_n_words(key, board, \
                words_by_length[key])

    # Creates a dictionary of scores for each word
    #   Example entry: { "ABC": [(9, [(0, 0), (0, 1), (0, 2)])] }
    #                    ^ WORD ^ List of paths
    words_scores: Dict[str, List[Tuple[int, List[Tuple[int, int]]]]] = dict()

    for n in paths_by_length.keys():
        for path in paths_by_length[n]:

            word = is_valid_path(board, path, words)

            if word is not None:
                tmp_score = get_path_score(path)
                
                if word not in words_scores:
                    words_scores[word] = []

                words_scores[word].append((tmp_score, path))

    paths = []

    for word in words_scores.keys():
        paths.append(max(words_scores[word], key=lambda x: x[SCORE_INDEX]))
    
    return [path[PATH_INDEX] for path in paths]


# === GLOBAL UTILS ===
def is_legal_path(board: List[List[str]], path: List[Tuple[int ,int]]) -> bool:
    """
    Checks if the given ${path} is legal
    """
    
    ROW = 0
    COLUMN = 1

    # If we got a ROW/COLUMN that's not within bounds
    for coord in path:
        if not (0 <= coord[ROW_INDEX] < len(board) and \
                0 <= coord[COLUMN_INDEX] < len(board[0])):
            return False

    for i, coord in enumerate(path[:-1]):
        next_coord = path[i+1]

        if not (abs(next_coord[ROW] - coord[ROW]) <= MAX_ROW_DISTANCE):
            return False
        
        if not (abs(next_coord[COLUMN] - coord[COLUMN]) <= MAX_COLUMN_DISTANCE):
            return False
    
    return True

def get_path_score(path: List[Tuple[int ,int]]) -> int:
    """
    Calculates the score given for a path to a word
    """
    
    return len(path)**2

def read_file(file_name: str) -> List[str]:
    """
    Reads the given file and returns a list of it's lines
    """
    
    with open(file_name, "r") as file:
        return file.read().splitlines()


# === UTILS ===
def __build_word_from_path(board: List[List[str]], path: List[Tuple[int ,int]]) \
        -> str:
    """
    A helper function that builds a word from the ${board} data according to
    coordinates from ${path}
    """

    word = ""

    for coord in path:
        word += board[coord[0]][coord[1]]

    return word

def __board_iterator(board: List[List[str]]) -> Generator:
    """
    A helper generator to create an iterator yielding tuples representing
    a coordinate in the board
    """

    for row in range(len(board)):
        for col in range(len(board[row])):
            yield row, col


def __bruteforce_paths(board: List[List[str]], current_path: List[Tuple[int ,int]], \
        recursion_logic) -> List[List[Tuple[int, int]]]:
    
    if len(current_path) == 0:
        raise ValueError(
            "An empty path was given, but a path must have a starting point.")

    paths = []
    last_cord = current_path[-1]

    BOARD_LENGTH, BOARD_WIDTH = len(board), len(board[0])

    # Looping over all adjacent coordinates to the last_cord and if it's a valid
    # coordinate (meaning it's within bounds and was not used before in the path)
    # we calculate all of its possible paths through the recursive helper function
    # and add it up to the list of paths
    for i in range(last_cord[0]-1, last_cord[0]+2):
        if i < 0 or i >= BOARD_LENGTH:
            continue

        for j in range(last_cord[1]-1, last_cord[1]+2):
            if j < 0 or j >= BOARD_WIDTH:
                continue

            new_cord = (i, j)
            if new_cord not in current_path:
                for path in recursion_logic(new_cord):
                    paths.append(path)

    return paths