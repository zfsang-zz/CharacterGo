import nltk   
from utils.file_io_helper import read_books_json
from utils.file_io_helper import read_book_nlp_html
import xml.etree.ElementTree as ET
import spacy
from collections import defaultdict
import re 

def find_matched_block(character_pairs,sentences):
    matched = defaultdict(list)
    for sent in sentences:
        sent = str(sent)

        for pair in character_pairs:
            search_go_to = pair
            m = ' .*? '.join(x for x in search_go_to)
            if re.search(m, str(sent)):
                matched[pair].append(sent) 
    return matched

def co_occurence(sentences):
    pair_sent = defaultdict(list)
    for sent in sentences:
        curr = nlp(sent.text)
        curr_name = []
        for ent in curr.ents:
            if ent.label_ == 'PERSON':
                name = ent.text
                size = len(name)
                if name[size/2]==' ' and name[:size/2] ==name[size/2+1:]:
                    name = name[:size/2]
                curr_name.append(name)

        if curr_name:
            pair = []
            prev = None
            for name_ in curr_name:
                if (not prev or prev!=name_) and len(curr_name)<2:
                    pair.append(name_)
                    prev = name_
            curr_name = tuple(sorted(curr_name))
            if len(curr_name)>1:
                pair_sent[curr_name].append(sent.text)
    return pair_sent


if __name__ == '__main__':
    clean = read_book_nlp_html() 
    # books = read_books_json('../data/SparkNotes_book_summary.json')
    # book0 = books[0]
    nlp = spacy.load('en')

    doc = nlp(clean)
    # sentences = list(doc.sents)
    # character_pairs = [('Winston','Julia'),('Winston',u'O\u2019Brien'.encode('utf-8'))]
    # block_1 = find_matched_block(character_pairs,sentences)
    # tree = ET.parse('../data/summary-parse/1.1984_summary.txt.xml')
    # root = tree.getroot()
    pair_test = co_occurence(doc.sents)