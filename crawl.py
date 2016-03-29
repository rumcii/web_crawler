import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def is_url(url):
    return urlparse(url).netloc != ''


def get_url(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    result = []

    for link in soup.find_all('a'):
        if is_url(link.get('href')) and link.get('href') is not2 None:
            result.append(link.get('href'))

    return result


def main():
    url = sys.argv[1]
    r = requests.get(url)

    html_doc = r.text

    for link in get_url(html_doc):
        print(link)


if __name__ == '__main__':
    main()
