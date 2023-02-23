import pickle
import requests as req

from typing import Dict
from urllib.parse import urlparse


def fix_url(url: str) -> str:
    """
    Fixes the given url
    """

    if not url.lower().startswith("https://"):
        url = "https://" + url

    if not url.endswith("/"):
        url += "/"
    
    return url

def get_source(url: str) -> str:
    """
    Queries a url and downloads it's source-code
    """
    
    res = req.get(url)

    return res.text


def is_absolute_path(url: str) -> bool:
    """
    Checks if the given url at ${url} is absolute
    """

    return bool(urlparse(url).netloc)

def is_relative_path(url: str) -> bool:
    """
    Checks if the given url at ${url} is relative
    """

    return not is_absolute_path(url)

def parse_relative_paths_from_file(file_name: str) -> list:
    """
    Loops over the given file in ${file_name} and appends all entries to a list
    """

    pages = []

    with open(file_name, "r") as file:
        for page in file:
            pages.append(page.strip())

    return pages


def save_dict_pickle_format(dict: Dict, target_file: str):
    """
    Saves the dictionary given in ${dict} in ${target_file} as a pickle file
    """

    with open(target_file, "wb") as file:
        pickle.dump(dict, file)

def load_dict_pickle_format(source_file: str) -> Dict:
    """
    Loads a dictionary from the given pickle-formatted file in ${source_file}
    """
    with open(source_file, "rb") as file:
        return pickle.load(file)