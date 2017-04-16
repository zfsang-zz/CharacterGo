import pandas as pd
import matplotlib.pyplot as plt
import json
import plotly
from textblob import TextBlob
import pickle
from .model import *

def plot_character_timeseries(character_offsets, character_labels, title='' ,y_axis='Times of Appearance', normalization_constant=None):
    """
    Plot characters' personal names specified in `character_labels` list as time series.
    
    :param character_offsets: dict object in form {'elizabeth': [123, 543, 4534], 'darcy': [205, 2111]}
    :param character_labels: list of strings that should match some of the keys in `character_offsets`
    :param normalization_constant: int
    """
    NUM_BINS = 10

    graph = {'data':[],'layout':dict(
                title=title,
                xaxis=dict(
                title='Related Position in Book'
        ),yaxis=dict(
                title='Times of Occurrence'
    ))
    }
    x = [character_offsets[character_label] for character_label in character_labels] 
    n, bins, patches = plt.hist(x, NUM_BINS, label=character_labels)    
    for i, a in enumerate(n):
        graph['data'].append(dict(
                    x=[float(x) / (NUM_BINS - 1) for x in range(len(a))],
                    y=a,
                    name = character_labels[i],
                    type='scatter'
                ))
    return graph

def plot_sent(ind_dict, pair_dict):
    graph = {'data':[],'layout':dict(
            title='Sentiment Trend',
                            xaxis=dict(
                title='Related Position in Book'
        ),yaxis=dict(
                title='Times of Appearance')
        
        )}
    max_sent = max( [ ii for i in ind_dict.values() for ii in i])
    pair_dict_polarity = {key: [[ch[0] for ch in pair_dict[key]],
                            [TextBlob(ch[1]).sentiment.polarity for ch in pair_dict[key]]] for key in pair_dict} 

    for key in pair_dict_polarity:
        graph['data'].append(dict(
            x = [xx/float(max_sent) for xx in pair_dict_polarity[key][0]],
            y = pair_dict_polarity[key][1],
            name = key,
            type='scatter'
        ))
    return graph


def plotly_multi(ind_dict,pair_dict):
    pair_dict_index = {key:[ch[0] for ch in pair_dict[key]] for key in pair_dict}
    pair_dict_sent = {key:[ch[1] for ch in pair_dict[key]] for key in pair_dict}
    graphs = [plot_character_timeseries(ind_dict, list(ind_dict.keys()),'Individual Character Occurrence Trend'),
    plot_character_timeseries(pair_dict_index, list(pair_dict_index.keys()),'Pair Charater Occurrence Trend'),
    plot_sent(ind_dict, pair_dict)]
    # for templating
    # ids = ['{}'.format(i) for i, _ in enumerate(graphs)]
    ids = ['1','2','3']
    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    return ids,graphJSON

def pair_relation(ind_dict, pair_dict):
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    pair_dict_sent = {key:[ch[1] for ch in pair_dict[key]] for key in pair_dict}

    # loaded_model.predict(['Before Sheriff Mapes can take Charlie in , Luke Will and Will crew arrive . They demand that Mapes hand Charlie over .'])
    pair_dict_pred= {key: loaded_model.predict([' '.join(pair_dict_sent[key])]) for key in pair_dict_sent}
    nodes = [{'id':key,value:32,label:key} for key in ind_dict ]
    edges = [{'from':key[0],'to':key[1],'title':'','label':pair_dict_pred[key][0]} for key in pair_dict_pred]
    nodesJSON = json.dumps(nodes)
    edgesJSON = json.dumps(edges)
    return nodesJSON,edgesJSON