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

# def co_occurence(sentences):
#     pair_sent = defaultdict(list)
#     for sent in sentences:
#         curr = nlp(sent.text)
#         curr_name = []
#         for ent in curr.ents:
#             if ent.label_ == 'PERSON':
#                 name = ent.text
#                 size = len(name)
#                 if name[size/2]==' ' and name[:size/2] ==name[size/2+1:]:
#                     name = name[:size/2]
#                 curr_name.append(name)

#         if curr_name:
#             pair = []
#             prev = None
#             for name_ in curr_name:
#                 if (not prev or prev!=name_) and len(pair)<2:
#                     pair.append(name_)
#                     prev = name_
#             pair = tuple(sorted(pair))
#         if len(pair)==2:
#             pair_sent[pair].append(sent.text)
#     return pair_sent

def sentence_out(sent):
    return ' '.join([w['word'] for w in sent['tokens']])


def co_occurence(doc):
    pair_sent = defaultdict(list)
    for sentence in doc.sentences:

        curr_name = []
        prev_ner = None
        for ent in sentence['tokens']:
            if ent['ner'] == 'PERSON':
                name = ent['word']
                size = len(name)
                if not prev_ner or prev_ner == name:
                    prev_ner = name
                else:
                    prev_ner += ' ' + name
            else:
                if prev_ner:
                    curr_name.append(prev_ner)
                prev_ner = None
        if prev_ner:
            curr_name.append(prev_ner)
            
        if curr_name:
            pair = []
            prev = None
            for name_ in curr_name:
                if (not prev or prev!=name_) and len(pair)<2:
                    pair.append(name_)
                    prev = name_
            pair = tuple(sorted(pair))
            
        if len(pair)==2:
            pair_sent[pair].append((sentence_out(sentence),sentiment[sentence['id']]))
    return pair_sent

def xml_analysis(xml_file,limit = 1):
    translate = {'Negative':-1,'Positive':1,'Neutral':0}
    xml = open(xml_file).read()
    annotated_text = A(xml)
    
    tree = html.fromstring(xml)
    sentiment = tree.xpath('//sentence/@sentiment')
    sentiment = [translate[key] for key in sentiment]

    pair_dict =co_occurence(annotated_text)
    
    avg_sent = lambda x:np.mean([y[1] for y in x])

    G = nx.Graph()
    for key,value in pair_dict.iteritems():
        appear = len(value)
        if appear>limit:
            G.add_edge(key[0],key[1], label='Connect:{},Sentiment:{}'.format(appear,avg_sent(value) ))
    
#     nxpd.draw(G, show='ipynb')
    
    return G

if __name__ == '__main__':
    # clean = read_book_nlp_html() 
    # with open('../data/summary-tag/1.1984_tag.txt','w') as f:
    #     f.write(clean)

    clean_full = read_book_nlp_html('../tools/book-nlp/data/output/1.1984_full.txt/1.1984_full.txt.html')
    with open('../data/summary-tag/1.1984_full_tag.txt','w') as f:
        f.write(clean_full)

    # books = read_books_json('../data/SparkNotes_book_summary.json')
    # book0 = books[0]
    # nlp = spacy.load('en')

    # doc = nlp(clean)
    # sentences = list(doc.sents)
    # character_pairs = [('Winston','Julia'),('Winston',u'O\u2019Brien'.encode('utf-8'))]
    # block_1 = find_matched_block(character_pairs,sentences)
    # tree = ET.parse('../data/summary-parse/1.1984_summary.txt.xml')
    # root = tree.getroot()
    # pair_test = co_occurence(doc.sents)