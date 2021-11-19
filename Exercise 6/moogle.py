import sys

from actions import moogle_crawler as crawler
from actions import moogle_page_rank as page_rank
from actions import moogle_words_dict as words_dict

if __name__ == '__main__':
    action = sys.argv[1]

    if action.lower() == "crawl":
        crawler.crawler(sys.argv[2:])
        
    elif action.lower() == "page_rank":
        page_rank.page_rank(sys.argv[2:])

    elif action.lower() == "words_dict":
        words_dict.words_dict(sys.argv[2:])