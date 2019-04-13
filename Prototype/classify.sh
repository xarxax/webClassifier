



#cd src/htmlExtraction
#scrapy crawl -a parameter='urlsToClassify.txt' htmlExtractor #this does the whole scraping process
#cd ../..
python3 src/extractText.py
python3 src/clean.py
#perform WE transformation
#unitize
#load model and predict an output
