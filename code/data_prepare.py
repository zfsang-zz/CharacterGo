import spacy
import pandas as pd
import numpy as np
import json
import pickle
from collections import OrderedDict
import re
from utils.file_io_helper import read_books_json, parse_book_nlp_html, match_character_text, unicode_normalizer
import glob
import os

family = ['father','mother','aunt','wife','daughter','sibling','twin','family','heir','ancestor',
          'brother','uncle','sister','niece','grand','cousin','adopt','relat','nephew','son','child','divorce']
friend = ['friend','playmate','widow','frien']
romance = ['ex','lover','love','girlfriend','attraction','boyfriend','affair','engage',
          'fiance','crush','date','sweet','partner','couple','flirt','marr']
enemy = ['enem','victim','traitor','compet','parties','riv','dislike','foe','death','counter',
         'murder','accuse','duel','conflicts','hate','foil','opposition','disguise','kill']
acquaintance = ['acqua','coworker','student','prof','pup','roommate','school','work','host','housemates','companion',
               'neighbor','roomate','wizard','ally','allies','flatmate','mate','group','miss','member','peasant',
               'coll','train','comrade','land']
service = ['fellow','assist','doctor','detect','devil','master','mistress','slave','rule','henchman',
           'employer','serv','lead','law','king','prison',',coach','proph','resear','edit','ward',
           'cook','sale','officer','boss','office','lord','emperor','interview','chief','support','advis',
          'nurse','man','owner','mentor','benef','manager','ruler','starbuck','super','tetrarch','tour',
          'counsel','judge','merchant','employ','flower','general','warder','house','soldier','maid','major','help',
           'patient','cook','ward','business','bank','tenant','keeper','captain','tutor','keeper','actor','buy','lend',
          'porter','caller','scout','hire','protect','guide','attorney','coach','caretaker','associate','advers',
          'interrogator','harpooner','henchman']
label_dict = OrderedDict([('enemy',enemy),('romance',romance),('family',family),('friend',friend),
                         ('acquaintance',acquaintance),('service',service)])

def clean_label(label):
    for key,value in label_dict.iteritems():
        for v in value:
            if re.search(v,label):
                return key
    return 'ambiguous'

def clean_all(label_dict):
    for key in label_dict:
        for pair in label_dict[key]:
            label_dict[key][pair] = clean_label(label_dict[key][pair])
    return label_dict



if __name__ == '__main__':
	pair_label = {}
	for html in  glob.glob('../tools/book-nlp/data/output-summary/*/*.html'):
		pair_dict, ind_dict = parse_book_nlp_html(html)
		key = os.path.basename(html).split('.')[0]
		pair_label[key] = parse_book_nlp_html(html)[0]
	pickle.dump( pair_label, open( "../data/pair_sentences.p","wb" ))





