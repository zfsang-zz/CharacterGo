import json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def write_pair_one_book(book_name_author, character_list):
    size = len(character_list)
    with open('../relationship2/{}.csv'.format(book_name_author),'w') as f:
        for i in xrange(size):
            for j in xrange(i+1,size):
                f.write(','.join([character_list[i],character_list[j],'']))
                f.write('\n')

def write_pair_all_book(books):
    for i in xrange(len(books)):
        write_pair_one_book('{}.{}'.format(i+1,books[i]['_id']),[x[0] for x in books[i]['characters']])

def read_data(json_file):
    '''
    INPUT:json array file
    OUTPUT: list of dict
    '''
    with open(json_file,'r') as f:
        return json.load(f)

def write_url(books):
    url_character = [x['url'] + 'characters.html' for x in books]

    with open('../data/character_urls.md','w') as f:
        for url in url_character:
            f.write(','.join([url]))
            f.write('  \n')

def write_book_level(books):
    url_character = [x['url'] + 'characters.html' for x in books]
    
    with open('../data/books.csv','w') as f:
        for book in books:
            f.write(','.join([book['name'],book['authors'],book['url'] + 'summary.html','']))
            f.write('  \n')

def write_all_summary(books):
    for i in xrange(len(books)):
        with open('../data/summary-text/{}.{}.txt'.format(i+1,re.sub('\s','_',books[i]['name'])),'w') as f:
            f.write(books[i]['summary'])


if __name__ == '__main__':
    # lst = ['A','B','C','D','E']
    # write_pair_one_book('testbook',lst)
    books = read_data('../data/book_summary3.json')
    # write_pair_all_book(books)
    # write_url(books)
    write_all_summary(books)