# Preliminary Proposal

This document is used to organize initial ideas on the final project.


## 1. CharacterGO: Character Relationship Detection and Visualization

### Description

Identifying relationships between people is fundamental for the understanding of literatures. Main characters may have very certain strong relationship such as love, family, enemy, friend with others.  Without knowing that, it's hard for machine or even human to understand the complicated stories of novels.  This project addresses the problem of inferring the polarity/type of relationships between people in novels summaries.    

Eventually, CharacterGo will be able to guide the interpretation of narrative events, explain character behaviors and steer the reader’s expectation about the plot using self-generated character relationship graphs.  As such, it can have value for applications such as document summarization and machine reading.  

The project is aimed to utilize NLP methods (concurrence, sentiment analysis, semantic analysis) and potential deep learning (RNN) to classify the characters' relationship of classical novels.  

### Problem to Solve
1. Tagging main characters and their interaction in long text
2. Extract linguistic and semantic features, as well as features based on the domain knowledge
3. Infer the strength and type of pair-wise connections among main characters from novels
4. Visualize the relationships in entity graphs

### How to Present
1. Slides
2. One-page web app showing the case-study of one novel like Harry Potter

### Next Step
**(Build a minimum viable product)**     
1. Scrape ~300 novels with the following information: book name, Full text, plot summary, character list, author, year
2. Get 5 main character from each book (plot summary) and record the pair-wise relationships by hand (10 pairs for each story)
3. For each story, going through the text (plot summary) to identify concurrence of characters that are in the main character list     
4. Use the count of concurrence and potentially other features assign a value of connections (weight of edge) of the character pairs  
5. Generate the relationship graph based on the pairwise connections scores   
**(If I have time, I will do the following steps)**     
6. Instead of predicting the magnitude of connections of character pairs, predict the relationship between them (5 categories: Family(Lovers, Relatives, Spouses), Friend/Coworkers,Leader/Leadee (king, queen, managers, employers...), Enemy, Stranger)
7. Use the self generated relationship table to measure the pair-wise relationship given
8. Fine-tune the models to get better score (log loss on the 5 categories) on predicting the pair-wise relationship
9. Generate relationship graph using pair-wise relationship categories instead of connection scores.
10. Use the full text instead of the plot summaries to redo the analysis
11. Apply this generalized model to movie scripts

### Metrics
1. Use log-loss/Precision/Recall to measure the multi-class classification of pair-wise character relationship
2. Visually compare generated character plot with the ones found online

### Data Source

#### Main Data Source
http://www.sparknotes.com/lit/  (finish creating web crawler for scraping the plot summaries and character information)

#### Additional Data Sources
CMU Movie scrips dataset
http://venturebeat.com/2016/02/18/facebook-releases-1-6gb-data-set-of-childrens-stories-for-training-its-ai/
http://cs.rochester.edu/nlp/rocstories/  
https://github.com/earlynovels  
http://dhresourcesforprojectbuilding.pbworks.com/w/page/69244469/Data%20Collections%20and%20Datasets

### Reference:
https://arxiv.org/pdf/1511.03012.pdf
http://www.umiacs.umd.edu/~hal/docs/daume16literary.pdf   
http://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf   
http://sujitpal.blogspot.com/2015/07/discovering-entity-relationships-in.html   
http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/    
https://cs.umd.edu/~miyyer/pubs/2016_naacl_relationships.pdf  





















### Obsolete


## O1. Fashion Finder: Clothing Recognition and Recommendation on images and video streams
### Description
The project is aimed to utilize deep learning (CNN) and computer vision methods to identify the clothing part of images/video streams and recommend similar clothing items to the user.

### Problem to Solve
1. Provide bounding box for clothing part on new images
2. Crop the clothing part (e.g. T-shirt/pants/shoes ) and search for similar clothing items
3. Potentially provide online product links based on the clothing image search

### How to Present
1. One-Page Web app using Flask framework
2. Video demo of the model using What Not to Wear (U.S. TV series) or Fashion show videos (show the bounding box of the clothing items and recommended items)
3. Slides   

### Next Step
- Sign the agreement to download the data from the Deep Fashion site
- Create Docker images for the Python 3 + Anaconda + Tensorflow + GPU environment
-  Start to work on the EDA of clothing image recognition (try both tradition computer vision method and CNN)

### Data Source
* [Deep Fashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)
  * 800,000 diverse fashion images ranging from well-posed shop images to unconstrained consumer photos.  
  * Second, DeepFashion is annotated with rich information of clothing items. Each image in this dataset is labeled with 50 categories, 1,000 descriptive attributes, bounding box and clothing landmarks.  
  * Third, DeepFashion contains over 300,000 cross-pose/cross-domain image pairs  
* [ImageNet Fall 2011 Release] (http://academictorrents.com/details/564a77c1e1119da199ff32622a1609431b9f1c47) for pre-training model   
  * 1.3 TB  
* (http://people.ee.ethz.ch/~lbossard/projects/accv12/index.html)
* [Large-scale Fashion (DeepFashion) Database  
](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)
* Scrape image data with labels from Amazon if necessary  

### Reference:
1. [Deep Learning for Fast and Accurate
Fashion Item Detection](
https://kddfashion2016.mybluemix.net/kddfashion_finalSubmissions/Deep%20Learning%20for%20Fast%20and%20Accurate%20Fashion%20Item%20Detection.pdf)
2. [Rapid Clothing Retrieval via Deep Learning of Binary
Codes and Hierarchical Search](http://www.iis.sinica.edu.tw/papers/song/18378-F.pdf)
3. [Convolutional Neural Networks for Fashion Classification and Object Detection](http://cs231n.stanford.edu/reports/BLAO_KJAG_CS231N_FinalPaperFashionClassification.pdf)
4. [Image-based Recommendations on Styles and Substitutes](https://cseweb.ucsd.edu/~jmcauley/pdfs/sigir15.pdf)
5. [MULTI-LABEL LEARNING WITH THE RNNS
FOR FASHION SEARCH](https://openreview.net/pdf?id=HyWDCXjgx)





## O2. Deep Personal Trainer

### Description
The project is aimed to utilize computer vision and machine learning methods to classify good work-out postures.

### Problem to Solve

### How to Present
1. Slides
2. One-page web app

### Next Step


### Data Source
http://human-pose.mpi-inf.mpg.de/#overview


### Reference:
http://pose.mpi-inf.mpg.de/#overview
https://arxiv.org/pdf/1607.03827.pdf
http://humaneva.is.tue.mpg.de/




## O3. 2016 Presidential Election Advertisement Video Analysis
### Description  
Predict the campaign party and event outcome.
### Problem to Solve
1. Video Feature Extraction through Factorization
2. Build Tree-Based Prediction Model (Binary/Continuous Outcome)
3. The correlation between Advertisement video and twitter trend in 2016 presidential election.
### How to Present
1.  One-page web visualization using Bootstrap, D3.js
2.  Slides

### Next Step
1. Download all the video contents
2. Start EDA on videos
3. Find or scrape related tweets

### Data Source
meta data in csv, all videos can be extracted from URLs.  
https://politicaladarchive.org/data/  
- 257722 advertisement records
- 109 unique video URL links (need to figure out how to get the rest videos without URL)
### Note
If any other well-labeled ad video dataset is found, may change the dataset.  

### Reference
1. [Large-scale Video Classification with Convolutional Neural Networks](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Karpathy_Large-scale_Video_Classification_2014_CVPR_paper.pdf)
2. [How-can-Machine-Learning-be-useful-for-analyzing-video](https://www.quora.com/How-can-Machine-Learning-be-useful-for-analyzing-video)
3. [Deep Learning of Invariant Features via Simulated
Fixations in Video](https://papers.nips.cc/paper/4730-deep-learning-of-invariant-features-via-simulated-fixations-in-video.pdf)  
4. [Deep Learning from Temporal Coherence in Video](https://ronan.collobert.com/pub/matos/2009_video_icml.pdf)  
5. [Non-Negative Matrix Factorization of Partial Track Data for Motion
Segmentation](https://ecse.rpi.edu/~rjradke/papers/cheriyadat-radkeiccv09.pdf)  

## O4. Trip Planner
### Description  
Provide trip route planner based on the preference of local attractions, food and professional photographing.
### Problem to Solve
1. Optimization of path of different locations on map with minimum of one location in each categories and different path weights and node weights(it's a NP-complete (hard) problem since don't have start/end point.  More easy to do Optimization on fixed start/end point, e.g. Dijkstra's algorithm )
2. Recommendation on trip route based on collaborate filtering
### How to Present
1. Web app only focus on the San Francisco Region
2. Slides

### Next Step
- Write Python Scrapy code to crawl locations with description, score and GPS info.
### Data Source
- TripAdvisor (need to scrape)
- Foursquare
- Booking (poor API)
- Flickr
- [GeoLife GPS Trajectories
](https://www.microsoft.com/en-us/download/details.aspx?id=52367)  

### Reference
1. [The Shortest Path to Happiness:
Recommending Beautiful, Quiet, and Happy Routes in the
City (Yahoo)](http://researchswinger.org/publications/quercia14_shortest.pdf)
2. [Photo2Trip: Generating Travel Routes from Geo-Tagged
Photos for Trip Planning](https://www.microsoft.com/en-us/research/wp-content/uploads/2010/01/24-2010-acmmm-photo2trip-mmfat06245-Xin.pdf)
3. [Exploiting Large-Scale Check-in Data to Recommend
Time-Sensitive Routes ](https://www.cs.uic.edu/~urbcomp2012/papers/UrbComp2012_Paper19_Hsieh.pdf)    



### O5. Food Type/Calories Recognition

### O6. Emotion Map: Image Sentiment Analysis with Geo-Information

### O7. Build A Self-Driving Model Car

### O8. Team Photo Facial Alignment   
