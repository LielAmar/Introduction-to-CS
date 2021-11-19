from typing import Dict

import moogle_helper as helper


def filter_pages_by_words(query: list, ranking_dict: Dict,
        words_dict: Dict) -> Dict:
    """
    Loops over all words in the given query at ${query} and removes all pages
    that do not contain all of the words in the query.
    """

    # Loading all pages
    filtered_pages = { page: ranking_dict[page] for page in ranking_dict.keys() }

    for page in filtered_pages.keys():
        found = False

        for word in words_dict.values():
            if page in word:
                found = True
        
        if not found:
            del filtered_pages[page]

    # Looping over all words given in the query string and filters out all
    # pages that do not contain the word
    for word in query:
        valid_pages = []

        if not word in words_dict:
            continue

        for page, occurances in words_dict[word].items():
            valid_pages.append(page)

        for page in filtered_pages.copy():
            if not page in valid_pages:
                filtered_pages.pop(page)

    return filtered_pages


def sort_pages_by_ranking_and_occurances(query: list, pages: Dict, words_dict: Dict) -> Dict:
    """
    Sorts the given list in ${pages} by their ranking in the given dictionary
    at ${ranking_dict} and by the amount of occurances of each word.
    """

    # Re-calculating the ranking of each page in the given page list at ${pages}
    # Calculated using the ranking of each page multiplied by the word with
    # the least amount of occurances for each page
    for page in pages.keys():
        least_occurances = 1

        for word in query[:]:
            if not word in words_dict.keys():
                continue

            occurances = words_dict[word][page]

            if occurances < least_occurances or least_occurances == -1:
                least_occurances = occurances

        pages[page] = least_occurances * pages[page]

    # Sorting the pages by their ranking
    pages = sorted(pages.items(), key=lambda x: x[1], reverse=True)

    return pages


def save_results_to_file(pages: Dict, max_results: int):
    # Saves the result to results.txt
    with open("results.txt", "a") as file:
        for item in pages[:max_results]:
            line = item[0] + " " + str(item[1])

            print(line)
            file.write(line + "\n")

        file.write("**********" + "\n")


def search(args: list) -> None:
    query = args[:-3]

    ranking_dict_file, words_dict_file, max_results = args[-3:]

    ranking_dict = helper.load_dict_pickle_format(ranking_dict_file)
    words_dict = helper.load_dict_pickle_format(words_dict_file)

    # Filters all pages and keeps only the pages that contain all words given in query
    filtered_pages = filter_pages_by_words(query, ranking_dict, words_dict)

    # Sorts the remaining pages by their ranking and occurances
    filtered_pages = sort_pages_by_ranking_and_occurances(query, filtered_pages,
            words_dict)

    save_results_to_file(filtered_pages, int(max_results))