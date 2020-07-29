"""
Dirty hacks for models building (because Yandex doesnt have good docs)
"""
from collections import defaultdict
from typing import List

import requests
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor

docs_url = 'https://yandex.com/dev/weather/doc/dg/concepts/forecast-test-docpage/'


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_lists(soup: BeautifulSoup) -> List[List[str]]:
    extractor = Extractor(soup)
    extractor.parse()
    return extractor.return_list()


def print_models(data: List[List[str]]):
    types = defaultdict(lambda: 'dict', **{
        'Object': 'dict',
        'Number': 'float',
        'String': 'str',
        'Boolean': 'bool',
    })

    for d in data[1:]:
        if d == ['Field', 'Description', 'Format']:
            print('\n----------\n')
            continue

        for doc_line in d[1].split('\n'):
            print(f'# {doc_line.strip(".")}')
        print(f'{d[0]}: {types[d[2]]}')


if __name__ == '__main__':
    soup = get_soup(docs_url)
    data = get_lists(soup)
    print_models(data)
