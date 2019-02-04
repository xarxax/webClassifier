#creates folder and creates text
#rm -rf datasetFeatures/*

numberToExtract=1112222
echo 'extracting '$numberToExtract
echo '----------------EXTRACTING TEXT FEATURES----------------'
python3 extractText.py $numberToExtract
echo '----------------EXTRACTING URL FEATURES----------------'
python3 extractUrls.py $numberToExtract
echo '----------------EXTRACTING IMAGE FEATURES----------------'
#python extractImgs.py $numberToExtract
