import xml.etree.ElementTree as ET
import sys

__author__ = 'guillem.gili.bueno'


urlDMOZ = 'https://dmoztools.net'
categories = sys.argv[1]


# ['Arts' ,'Business','Computers','Games','Health','Home','News','Recreation'
#,'Reference','Science','Shopping','Society','Sports']

file = open('content.rdf.u8','r')

outfile=open('catAndUrl.txt','wr')

categoryAttr ='{http://www.w3.org/TR/RDF/}id'
urlAttr ='{http://www.w3.org/TR/RDF/}resource'

# get an iterable
context = ET.iterparse(file, events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
event, root = context.next()

for event, elem in context:
    if elem.tag.split('}')[1] != 'Topic' or elem.attrib[categoryAttr] == '':
        continue
    print(elem.attrib[categoryAttr])
    cat = elem.attrib[categoryAttr].encode('utf-8')
    cat =cat.split('/')[1]
    if cat in categories:
        for child in elem:
            if child.tag.split('}')[1] != 'link':
                continue
            url = child.attrib[urlAttr].encode('utf-8')
            outfile.write(str(cat)  + ',' + str(url)  + '\n')
    root.clear()
