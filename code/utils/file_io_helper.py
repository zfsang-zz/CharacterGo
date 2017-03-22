import json
from bs4 import BeautifulSoup
import spacy
import re
def read_books_json(json_file):
    '''
    INPUT:json array file
    OUTPUT: list of dict
    '''
    with open(json_file,'r') as f:
        return json.load(f)

def read_book_nlp_html(file='/Users/codehi/Projects/Galvanize/Capstone/tools/book-nlp/data/output/1.1984.txt/1.1984.txt.html'):
    with open(file,'r') as f:
        html = f.read()
        html_character_list, html_tag = html.split('<h1>Text</h1>')
        soup = BeautifulSoup(html_tag)

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        clean_text = re.sub('\S+ \((\S+)\)', '\\1', text)
        return clean_text



def read_tag_xml():
	pass
	