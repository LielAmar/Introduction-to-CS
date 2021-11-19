import sys

import moogle_crawler as crawler
import moogle_page_rank as page_rank
import moogle_words_dict as words_dict
import moogle_search as search

if __name__ == "__main__":
    action = sys.argv[1]

    if action.lower() == "crawl":
        crawler.crawler(sys.argv[2:])
        
    elif action.lower() == "page_rank":
        page_rank.page_rank(sys.argv[2:])

    elif action.lower() == "words_dict":
        words_dict.words_dict(sys.argv[2:])

    elif action.lower() == "search":
        search.search(sys.argv[2:])