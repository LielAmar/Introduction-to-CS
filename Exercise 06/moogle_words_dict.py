import bs4
import urllib.parse 

from typing import Dict

import moogle_helper as helper


def get_words_of_page(html: str) -> list:
    """
    Returns all the words in the given html code
    """

    words = []

    soup = bs4.BeautifulSoup(html, "html.parser")
    p_tags = soup.find_all("p")

    for p_tag in p_tags:
        for word in p_tag.text.split():
            words.append(word)

    return words

def load_words_dictionary(base_url: str,
        file_name: str) -> Dict[str, Dict[str, int]]:
    """
    Loads the words data through the URLs built from ${base_url} and relative
    paths in the given file, ${file}
    """

    pages = helper.parse_relative_paths_from_file(file_name)

    dict: Dict[str, Dict[str, int]] = {}


    # Loops over all pages, downloads thier source, gets their words list
    # and adds them to the dictionary
    for page in pages:
        page_url = urllib.parse.urljoin(base_url, page)
        source = helper.get_source(page_url)

        words = get_words_of_page(source)

        # Loops over all words of all pages and updates the amount of occurences
        # of each word in each page in the dictionary
        for word in words:
            if word not in dict:
                dict[word] = {}
                
            amnt_of_appearances = dict[word].get(page, 0) + 1
            dict[word][page] = amnt_of_appearances

    return dict


def words_dict(args: list) -> None:
    base_url, index_file, out_file = args
    
    # Fixes the given base url
    base_url = helper.fix_url(base_url)

    # Builds the words dictionary
    words_dict = load_words_dictionary(base_url, index_file)

    # Saves the built traffic dict
    helper.save_dict_pickle_format(words_dict, out_file)