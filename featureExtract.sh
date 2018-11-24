#creates folder and creates text
#rm -rf datasetFeatures/*

echo '----------------EXTRACTING TEXT FEATURES----------------'
#python extractText.py
echo '----------------EXTRACTING URL FEATURES----------------'
python extractUrls.py
echo '----------------EXTRACTING IMAGE FEATURES----------------'
