# webClassifier

This project is a web classifier that give us the category that most fits a website given its links, text and images.
The dataset used for this project can be found in https://web.archive.org/web/20170303013959/http://dmoz.org/rdf.html

To test the files to run remember to use 'chmod 755 filetorun.sh'

## Files to run

### scrapAndExtract.sh
The purpose of this script is to get the urls and their category from our original source and then extract the content of the amount it wants.
This script takes the content from content.rdf.u8 and gets the urls from the 9 preestablished categories: Arts,Business,Computers,Games,Health,Home,Recreation,Science,Sport
Then it generates a file with the pairs category,url

Once that is done it chooses N pairs at random and writes them.

Then it extracts the html using Scrapy and writes the content for each web in the following format:
category
url
htmlCode

### extractText.sh
This file gets the html documents and gets the features we want for our algorithm. It will save them in a folder for each web format. These folders will be in datasetFeatures

First it gets their text and generates the folder for each web.



## issues
This pages html was badly parsed.
Business
http://www.alaturfgrass.org/
<html><HEAD>

</HEAD><FRAMESET border='0' ROWS='*,1'> <FRAME SRC='http://alturfgrass.org'><FRAME SRC='blank.html'> </FRAMESET> </html>xarxax@xarxax-To-be-filled-by-O-E-M:~/tfg$
