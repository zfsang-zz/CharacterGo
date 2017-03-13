import requests
from bs4 import BeautifulSoup
from lxml import html
import re
from collections import defaultdict

def search_main():
	letters = 'abcdefghijklmnopqrstuvwxyz' 
	book_urls = []
	book_names = []
	book_authors = []
	res = defaultdict(dict)
	for ch in letters:
		index_url = 'http://www.sparknotes.com/lit/index_{}.html'.format(ch)
		curr_urls,curr_names,curr_authors = search_index(index_url)
		book_urls.extend(curr_urls)
		book_names.extend(curr_names)
		book_authors.extend(curr_authors)

	for i in xrange(len(book_urls)):
		res[book_names[i]]['name'] = book_names[i]
		res[book_names[i]]['author'] = book_authors[i]
		res[book_names[i]]['url'] = book_urls[i]
		if book_urls[i] != '#':
			summary_url = book_urls[i] +

	return list(zip(book_urls,book_names,book_authors))

def search_index(index_page):
	url = 'http://www.sparknotes.com/lit/index_a.html'
	page = requests.get(url)
	tree = html.fromstring(page.content)
	next_urls = tree.xpath('//p[@class="clearfix"]//a//@href')
	next_names = tree.xpath('//span[@class="left"]/text()')
	next_authors = tree.xpath('//span[@class="right text-color"]/text()')
	return next_urls,next_names,next_authors

def search_content(url='http://www.sparknotes.com/lit/1984/summary.html'):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	characters = tree.xpath('//div[@id = "plotoverview"][@class ="studyGuideText"]//p')
	paragraphs = [re.sub('\n','',p.text_content()) for p in paragraphs]
	return paragraphs

def search_character(url='http://www.sparknotes.com/lit/1984/characters.html'):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	names = tree.xpath('//div[@id = "characterlist"]//div[@class = "content_txt"]/@id')
	paragraphs = tree.xpath('//div[@id = "characterlist"]//div[@class = "content_txt"]/*[not(name()="p")]')
	descriptions = [re.sub('\n','',p.text_content()) for p in paragraphs]
	# descriptions = tree.xpath('//div[@id = "characterlist"]//div[@id = "content_txt"]/text()')
	
	return list(zip(names,descriptions))


if __name__ == '__main__':
	books = search_main()
	with open("books_list.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(books) 
	with open("1984.txt", "wb") as f:
	    f.write("/n".join(res).encode('ascii','ignore')) 