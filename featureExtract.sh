#creates folder and creates text
rm -rf datasetFeatures/*

echo '----------------EXTRACTING TEXT FEATURES----------------'
python extractText.py
echo '----------------EXTRACTING URL FEATURES----------------'
echo '----------------EXTRACTING IMAGE FEATURES----------------'
