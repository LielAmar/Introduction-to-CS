import bs4
import urllib.parse 

from typing import Dict

import moogle_helper as helper


def get_refrences_of_page(html: str, only_relatives: bool = False) -> list:
    """
    Returns all the reference links in the given html code.
    If ${only_relatives} is True, this function returns only relative links
    """

    references = []

    soup = bs4.BeautifulSoup(html, "html.parser")
    p_tags = soup.find_all("p")

    for p_tag in p_tags:
        a_tags = p_tag.find_all("a")

        for a_tag in a_tags:
            if a_tag.has_attr("href") and len(a_tag.get("href")) != 0:
                href = a_tag.get("href")

                if (only_relatives and helper.is_relative_path(href)
                        or not only_relatives):
                    references.append(href)

    return references


def load_traffic_dictionary(base_url: str,
        file_name: str) -> Dict[str, Dict[str, int]]:
    """
    Loads the traffic data through the URLs built from ${base_url} and relative
    paths in the given file, ${file}
    """

    pages = helper.parse_relative_paths_from_file(file_name)

    dict: Dict[str, Dict[str, int]] = { page: {} for page in pages }

    # Loops over all pages, downloads thier source, gets their reference list
    # and adds them to the dictionary
    for page in pages:
        page_url = urllib.parse.urljoin(base_url, page)
        source = helper.get_source(page_url)

        references = get_refrences_of_page(source, True)

        # Loops over all references of all pages and updates the amount of occurences
        # of each reference in the dictionary
        # If a certain reference is not included in ${file_name}, we skip it
        # If we have a refer
        for reference in references:
            if not reference in pages:
                continue

            amnt_of_references = dict[page].get(page, 0) + 1
            dict[page][reference] = amnt_of_references

    return dict


def crawler(args: list) -> None:
    base_url, index_file, out_file = args

    # Fixes the given base url
    base_url = helper.fix_url(base_url)

    # Builds the traffic dictionary
    traffic_dict = load_traffic_dictionary(base_url, index_file)

    # Saves the built traffic dict
    helper.save_dict_pickle_format(traffic_dict, out_file)