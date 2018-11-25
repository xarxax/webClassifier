#creates folder and creates text
#rm -rf datasetFeatures/*

numberToExtract=9
echo 'extracting '$numberToExtract
echo '----------------EXTRACTING TEXT FEATURES----------------'
#python extractText.py $numberToExtract
echo '----------------EXTRACTING URL FEATURES----------------'
#python extractUrls.py $numberToExtract
echo '----------------EXTRACTING IMAGE FEATURES----------------'
python extractImgs.py $numberToExtract
