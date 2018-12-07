#rdf obtained in https://web.archive.org/web/20170303013959/http://dmoz.org/rdf.html


# we extract info from the rdf base file

for Category in Arts Business Computers Games Health Home News Recreation Reference Science Shopping Society Sports
do
    #this will turn our rdf to a simpler file format
    python rdfToPairs.py $Category



    echo '----------------RANDOMLY PICKING SITES----------------'


    #this limits our results to the final dataset we will work onto
    total=$(wc -l catAndUrl.txt) #get the total number of lines (websites)
    python chooseNPages.py  $total $total # last parameter is number of webs we want

    echo '----------------BEGINNING WEBSITE EXTRACTION----------------'
    #now we must extract the websites
    #rm -rf ./dataset/*    #clean previously extracted
    cd htmlExtraction
    scrapy crawl htmlExtractor #this does the whole scraping process
done
