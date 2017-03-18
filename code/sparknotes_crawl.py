import requests
from bs4 import BeautifulSoup
from lxml import html
import re
from collections import defaultdict
import json
import numpy as np
import pymongo
import tqdm
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def init_mongo_client():
    # Initiate Mongo client
    client = pymongo.MongoClient()

    # Access database created for these articles
    db = client.books

    # Access collection created for these articles
    coll = db.book_summary

    # Access articles collection in db and return collection pointer.
    return db.book_summary


def search_main(coll):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    book_urls = []
    book_names = []
    book_authors = []
    # res = defaultdict(dict)
    for ch in letters:
        index_url = 'http://www.sparknotes.com/lit/index_{}.html'.format(ch)
        curr_urls,curr_names,curr_authors = search_index(index_url)
        book_urls.extend(curr_urls)
        book_names.extend(curr_names)
        book_authors.extend(curr_authors)
    size = len(book_urls)
    print "Find {} books on SparkNotes, Start Scraping".format(size)
    for i in tqdm.tqdm(range(size)):
        # remove try except
        summary = ''
        characters = {}
        if book_urls[i] != '#':
            summary_url = book_urls[i] + '/summary.html'
            character_url = book_urls[i] + '/characters.html'
            summary = search_content(summary_url)
            characters = search_character(character_url)
        else:
            pass
        # try :
        book = {'_id':'{} ({})'.format(book_names[i],book_authors[i]),'name':book_names[i],
        'url':book_urls[i],'authors':book_authors[i],'summary':summary,'characters':characters }
        coll.insert(book,check_keys=False)
        # except:
        #     continue
     

def search_index(url = 'http://www.sparknotes.com/lit/index_a.html'):
    # try except here
    page = requests.get(url)
    tree = html.fromstring(page.content)
    next_urls = tree.xpath('//p[@class="clearfix"]//a//@href')
    next_names = tree.xpath('//span[@class="left"]/text()')
    next_authors = tree.xpath('//span[@class="right text-color"]')
    next_authors = [x.text if x.text else '' for x in next_authors]
    extra = tree.xpath('//li[@class = "read-sparknote"]//a/@href')
    extra_i = 0
    for i in xrange(len(next_urls)):
        if next_urls[i] == '#':
            next_urls[i] = extra[extra_i]
            extra_i + 1 
    return next_urls,next_names,next_authors

def search_content(url='http://www.sparknotes.com/lit/1984/summary.html'):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    paragraphs = tree.xpath('//div[@id = "plotoverview"][@class ="studyGuideText"]//p')
    paragraphs = '\n'.join([re.sub('\n','',p.text_content()) for p in paragraphs])
    return paragraphs

def search_character(url='http://www.sparknotes.com/lit/2001/characters.html'):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    names = tree.xpath('//div[@id = "characterlist"]//div[@class = "content_txt"]/@id')
    paragraphs = tree.xpath('//div[@id = "characterlist"]//div[@class = "content_txt"]/text()[normalize-space()]')
    descriptions = paragraphs
    # descriptions = [re.sub('\n','',p.text_content()) for p in paragraphs]
    # descriptions = tree.xpath('//div[@id = "characterlist"]//div[@id = "content_txt"]/text()')
    return dict(zip(names,descriptions))


if __name__ == '__main__':
    book_summary = init_mongo_client()
    search_main(book_summary)
    # with open('result.json', 'w') as f:
    #   json.dump(books, f)

    # with open("books_list.csv", "wb") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(books)
    # with open("1984.txt", "wb") as f:
    #     f.write("/n".join(res).encode('ascii','ignore'))
