from .vis_helper import plot_character_timeseries, plotly_multi,pair_relation
from .file_io_helper import unicode_normalizer, match_character_text, parse_book_nlp_html,subprocess_cmd
# from app.crawler.crawler import crawler
from flask import render_template, request,jsonify, redirect,url_for
from random import randint
from . import app
import json
import subprocess
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pickle
# index view function suppressed for brevity


# index page
@app.route("/")
def show_index_page():
    return render_template('index.html')

# index page
@app.route("/login.html")
def show_login_page():
    return render_template('login.html')

# result page
@app.route("/result", methods=['GET'])
def result():
    text = request.args.get('location')
    # with open("../tools/book-nlp/data/summary-text/tmp.txt",'wb') as f:
    #     f.write(unicode_normalizer(text))
    # # subprocess_cmd('cd ../tools/book-nlp;sh run_one_book.sh tmp.txt')
    # html = "../tools/book-nlp/data/output/tmp.txt/tmp.txt.html"
    html = './app/templates/tmp.txt.html'
    with open(html,'r') as f:
        parsed_html = f.read()
    pair_dict, ind_dict = parse_book_nlp_html(html) 

    # print(plot_character_timeseries(pair_dict, pair_dict.keys()))   
    ids,graphJSON=plotly_multi(ind_dict,pair_dict)
    # nodesJSON,edgesJSON = pair_relation(ind_dict, pair_dict)

    # ids =jsonify(ids)
    # return jsonify(ids=ids, graphJSON=graphJSON)
    # return redirect(url_for('test',graphJSON=graphJSON))
    return redirect(url_for('result2',graphJSON=graphJSON))#,nodesJSON=nodesJSON,edgesJSON=edgesJSON))
    
    # print(plotly_multi(pair_dict, ind_dict))
    # return render_template('result.html',ids=ids,graphJSON=graphJSON)
    # return render_template('result.html',text = out)#, locations=locations,lat=loc_latlon['lat'],lon=loc_latlon['lng'])
    # return redirect(url_for('result2'))

    
@app.route("/result2", methods=['GET'])
def result2():
    # ids = request.args.get('ids')
    graphJSON = request.args.get('graphJSON')
    nodesJSON = request.args.get('nodesJSON')
    edgesJSON = request.args.get('edgesJSON')
    return render_template('result2.html',graphJSON=graphJSON)#,nodesJSON=nodesJSON,edgesJSON=edgesJSON)

@app.route("/test", methods=['GET'])
def test():
    # ids = request.args.get('ids')
    graphJSON = request.args.get('graphJSON')
    return render_template('test.html',graphJSON=graphJSON)

@app.route("/tmp")
def show_parsed():
    return render_template('tmp.txt.html')

