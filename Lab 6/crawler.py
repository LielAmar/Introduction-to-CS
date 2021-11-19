import sys
import requests
import bs4

def download_page(url):
    response = requests.get(url)
    
    return response.text # html

def get_refrences_of_page(html, trimmed_url):
    references = []

    soup = bs4.BeautifulSoup(html, 'html.parser')
    p_tags = soup.find_all('p')

    for p_tag in p_tags:
        a_tags = p_tag.find_all('a')

        for a_tag in a_tags:
            href = a_tag.get('href')
            if not "https://" in href:
                href = trimmed_url + href
            references.append(href)

    return references

if __name__ == "__main__":
    script, url = sys.argv

    if not "https://" in url:
        url = "https://" + url

    html = download_page(url)
    
    url_parts = url.split("/")
    trimmed_url = (url_parts[0] + "/" + url_parts[1] + "/" + url_parts[2])
    
    print(trimmed_url)
    references = get_refrences_of_page(html, trimmed_url)
    
    for reference in references:
        print(reference)