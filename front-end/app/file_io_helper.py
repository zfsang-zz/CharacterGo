import json
import spacy
import re
import unicodedata
import pandas as pd
from fuzzywuzzy import fuzz
import spacy
import itertools
from collections import defaultdict
import subprocess
from bs4 import BeautifulSoup
def read_books_json(json_file):
    '''
    INPUT:json array file
    OUTPUT: list of dict
    '''
    with open(json_file,'r') as f:
        return json.load(f)


def parse_book_nlp_html(file='/Users/codehi/Projects/Galvanize/Capstone/tools/book-nlp/data/output/1.1984_full.txt/1.1984_full.txt.html'):
    with open(file,'r') as f:
        html = f.read()
        html_character_list, html_tag = html.split('<h1>Text</h1>')
        soup = BeautifulSoup(html_tag, "lxml")

        # clean the character list
        characters = html_character_list.split('</h1>')[1].split('<br />')[:-1]
        parse_ln = lambda x: ([a.strip() for a in re.findall(r'([A-Za-z\s\-\.]+)\(\d+\)',x.split('\t')[1])],x.split('\t')[0])
        characters = [parse_ln(ln) for ln in characters]
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # # get text
        text = soup.get_text()
        # # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = ' '.join(chunk for chunk in chunks if chunk)
        # clean_text = re.sub('\S+ \((\S+)\)', '\\1', text)
        # return clean_text
        pair_dict,individual_dict = match_character_text(characters,text,top = 5)
        return pair_dict,individual_dict

def match_character_text(characters,text,top = 5):
    nlp = spacy.load('en')
    character_list = {ch[0][0]:ch[0] for ch in characters[:top]}
    parsed = nlp(text)
    pair_dict = defaultdict(list)
    individual_dict = defaultdict(list)
    for i,sent in enumerate(parsed.sents):    
        curr_character = set()
        curr_text =sent.text
        for ch_key in character_list:
            ch_names = character_list[ch_key]
            for name in ch_names:
                if name in curr_text:
                    curr_character.add(ch_key)
                    break
        for ch in curr_character:
            individual_dict[ch].append(i)
        for ch1,ch2 in itertools.combinations(list(curr_character),2):
            pair_dict[tuple(sorted([ch1,ch2]))].append((i,curr_text))
    return pair_dict,individual_dict
            
        
def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """
def unicode_normalizer(text):
    text =text.replace(u"\u2019", "'")
    normal = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
    return normal

def read_tag_xml():
	pass
	