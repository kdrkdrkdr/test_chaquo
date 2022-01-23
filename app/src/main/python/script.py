# from novel_reader import NovelReader
# from _requirement_func import *

# a = p.translate('私は私のことが好きです', 'ko', 'ja')
# print(a)

import requests
def main(url):
    return requests.get(url).text
    # n = NovelReader(url)
    # return n.get_big_title()