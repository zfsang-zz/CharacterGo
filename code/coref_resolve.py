from utils.file_io_helper import *
import glob
import os

if __name__ == '__main__':
	for html in  glob.glob('../tools/book-nlp/data/output/*/*.html'):
		with open('../data/summary-coref/{}.txt'.format(os.path.basename(html)),'w') as f:
			f.write(unicode_normalizer(read_book_nlp_html(html)))
	