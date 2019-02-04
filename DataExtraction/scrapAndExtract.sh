#rdf obtained in https://web.archive.org/web/20170303013959/http://dmoz.org/rdf.html


# we extract info from the rdf base file
for entry in $`ls urlSplit`
do
  echo "File " $entry
  cd htmlExtraction
  scrapy crawl -a parameter=$entry htmlExtractor #this does the whole scraping process
  ps -a| grep scrapy
  #echo $?
  #echo $(`ps -a| grep scrapy`)
  #echo 'done'
  #while $`ps -a| grep scrapy` !=''
  #do
  #echo 'waiting'
  #sleep 2
  #done
  cd ..
  #echo 'first loop'
  #break
done
