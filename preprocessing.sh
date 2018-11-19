# we extract info from the rdf base file

#this will turn our rdf to a simpler file format
#python rdfToPairs.py

#get the total number of lines (websites)
total=$(wc -l catAndUrl.txt)

#this limits our results to the final dataset we will work onto,
#we will have at most 3k webs
python chooseNPages.py  $total 3000
