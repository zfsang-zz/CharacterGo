from utils.file_io_helper import read_books_json
from utils.file_io_helper import read_book_nlp_html
import pandas as pd
from fuzzywuzzy import fuzz
from shutil import copyfile
import unicodedata

""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """
def unicode_normalizer(text):
    text =text.replace(u"\u2019", "'")
    normal = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
    return normal

def match_novel(lst,target_lst):
	# set1 = set(lst)
	# set2 = set(target_lst)
	# first_match = set1&set2
	# set1 -= first_match
	# set2 -= first_match
	additional_match = []
	for num1,i in enumerate(lst):
		for num2,j in enumerate(target_lst):
			if fuzz.ratio(i,j)>80:
				additional_match.append((num1+1,i,num2+1,j))
	return additional_match



if __name__ == '__main__':
	books = read_books_json('../data/book_summary3.json')
	book_name = [unicode_normalizer(book['name']) for book in books]
	book_list = pd.read_csv('../data/additional/book_data.csv')['title'].dropna().tolist()
	overlap = match_novel(book_name,book_list)
	with open('../data/full-book-list.txt','w') as f:
		for num1,b1,num2,b2 in overlap:
			f.write("{}.{}\t{}\t{}\n".format(num1,b1,num2,b2))

	unmatched = []
	for num1,b1,num2,b2 in overlap:
		for suffix in ['','-0','-8']:
			try: 
				copyfile('/Volumes/Transcend/ebooks-unzipped/{}{}.txt'.format(num2,suffix), 
				'../data/full-text-match/{}.{}.txt'.format(num1,b1.decode('utf-8')))
			except:
				unmatched.append((num1,b1,num2,b2))
				print("{}.{}\t{}\t{}\n".format(num1,b1,num2,b2))