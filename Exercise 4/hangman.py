#################################################################
# FILE : hangman.py
# WRITER : Liel Amar, lielamar, 211771993
# EXERCISE : intro2cs2 ex4 2021
# DESCRIPTION: A simple program that mimics the Hangman game
# # STUDENTS I DISCUSSED THE EXERCISE WITH: Amir Debby
# WEB PAGES I USED: 
#   - https://stackoverflow.com/questions/394809/
# NOTES: 
#################################################################

import hangman_helper

import copy

def update_word_pattern(word, pattern, letter):
    """
    Updates the pattern of the given word
    """
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + letter + pattern[i+1:]
    
    return pattern

def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Filters the list words to only words matching ${pattern}
    by length, characters and wrong guess
    """
    words = [word for word in words if len(word) == len(pattern)]


    for i in range(len(pattern)):   
        words = [word for word in words if 
                (pattern[i] == "_" and not word[i] in pattern) 
                or word[i] == pattern[i]]

    for wrong_guess in wrong_guess_lst:
        words = [word for word in words if not wrong_guess in word]

    return words


def run_single_game(words_list, score):
    """
    Runs a single Hangman Game
    """
    
    word = hangman_helper.get_random_word(words_list) 
    pattern = "_" * len(word)

    wrong_guesses = list()
    state_message = "Hangman Started! :)"

    while score > 0 and pattern != word:
        hangman_helper.display_state(pattern, wrong_guesses, score, state_message)

        input_type, input_value = hangman_helper.get_input()

        if input_value in wrong_guesses:
            continue

        if input_type == hangman_helper.LETTER:
            pattern, score, state_message = handle_letter_input(input_value, word, pattern, wrong_guesses, score)
        elif input_type == hangman_helper.WORD:
            pattern, score, state_message = handle_word_input(input_value, word, pattern, score)
        elif input_type == hangman_helper.HINT:
            score, state_message = handle_hint_input(words_list, pattern, wrong_guesses, score)

    state_message = ("Wow, you actually beat the game! Well played!"
            if score > 0 else "You've lost :( Hidden word: " + word)
    hangman_helper.display_state(pattern, wrong_guesses, score, state_message)

    return score

def handle_letter_input(input_value, word, pattern, wrong_guesses, score):
    """
    Handles the game step when a letter is being given by the user
    """

    state_message = "Nice Guess!"

    if len(input_value) > 1 or not input_value.isalpha() or not input_value.islower():
        state_message = "Invalid input, moving to next round!"
    
    elif input_value in pattern:
        state_message = "Already used letter, moving to next round!"
    
    else:
        score -= 1
        
        if input_value in word:
            pattern = update_word_pattern(word, pattern, input_value)
            occurences = word.count(input_value)
                
            score += (occurences * (occurences + 1))//2
        else:
            wrong_guesses.append(input_value)
            state_message = word
    
    return pattern, score, state_message

def handle_word_input(input_value, word, pattern, score):
    """
    Handles the game step when a guess for the word
    is being given by the user
    """

    state_message = "Nice guess!"

    score -= 1

    # Guess was correct
    if input_value == word:
        remained_hidden_letters = len([i for i in word if not i in pattern])
        score += int((remained_hidden_letters*(remained_hidden_letters+1))//2)

        pattern = word
    else:
        state_message = "Ahh, your guess was wrong :("

    return pattern, score, state_message

def handle_hint_input(words_list, pattern, wrong_guesses, score):
    """
    Handles the game step when the user asked for a hint
    """

    state_message = "You've asked for a hint. You should be able to find it above ^"
    score -= 1

    filtered = filter_words_list(copy.copy(words_list),
            pattern, wrong_guesses)

    trimmed_filtered = filtered

    if len(filtered) > hangman_helper.HINT_LENGTH:
        trimmed_filtered = list()

        for i in range(0, hangman_helper.HINT_LENGTH):
            index = i*len(filtered)//hangman_helper.HINT_LENGTH
            
            trimmed_filtered.append(filtered[index])

    hangman_helper.show_suggestions(trimmed_filtered)
    return score, state_message


def main():
    loaded_words = hangman_helper.load_words()

    score = hangman_helper.POINTS_INITIAL
    games_played = 0

    while True:
        score = run_single_game(loaded_words, score)
        games_played += 1
        
        if score > 0:
            if hangman_helper.play_again("""
                    Wanna play another round?\n
                    So far you've played """ + str(games_played) + """ rounds!\n
                    Your total points are: """ + str(score)):
                continue
        else:
            if hangman_helper.play_again("""
                    Wanna play a new game?\n
                    You've lasted a total of """ + str(games_played) + """ rounds!\n
                    Your total points are: """ + str(score)):
                
                score = hangman_helper.POINTS_INITIAL
                games_played = 0
                continue
 
        break

if __name__ == "__main__":
    main()