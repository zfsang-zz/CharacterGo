mongoexport --db books --collection book_summary2 --out book_summary2.json --host 127.0.0.1 --port 27017 --jsonArray

java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000


java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,sentiment -filelist filelist.txt -outputDirectory

./runjava novels/BookNLP -doc data/originalTexts/dickens.oliver.pg730.txt -printHTML -p data/output/dickens -tok data/tokens/dickens.oliver.tokens -f


java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,sentiment -file ../../data/summary-tag/1.1984_tag_clean.txt -outputDirectory ../../data/summary-tag/


java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators -annotators tokenize,ssplit,pos,lemma,parse,sentiment -file ../../data/summary-tag/1.1984_tag_clean.txt -outputDirectory ../../data/summary-tag/