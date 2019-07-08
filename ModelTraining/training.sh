#######################DOCS####DATASET##################LAYERS####UNITS##EPOCHS ###dropout
python3 NNFeeding3.py 200000 unitizedgloveDatasetNoNews  5  150 30 0.2
python3 NNFeeding3.py 200000 unitizedlexvecDatasetNoNews  5  150 30 0.2
python3 NNFeeding3.py 200000 unitizedword2vecDatasetNoNews  5  150 30 0.2

python3 NNFeeding3.py 200000 unitizedgloveDatasetNoNews  5  200 30 0.2
python3 NNFeeding3.py 200000 unitizedlexvecDatasetNoNews  5  200 30 0.2
python3 NNFeeding3.py 200000 unitizedword2vecDatasetNoNews  5  200 30 0.2

#python3 NNFeeding3.py 300000 unitizedgloveDatasetNoNewsRefShop  5  300 100 0.8
#python3 NNFeeding3.py 300000 unitizedgloveDatasetNoNewsRefShop  5  300 100 0.4
#python3 NNFeeding3.py 300000 unitizedlexvecDatasetNoNewsRefShop  5  300 100 0.5

#python3 NNFeeding3.py 300000 unitizedgloveDatasetNoNews  5  300 100
#python3 NNFeeding3.py 300000 unitizedlexvecDatasetNoNews  5  300 100
#python3 NNFeeding3.py 300000 unitizedword2vecDatasetNoNews  5  300 100

#python3 NNFeeding2.py 5000 lexvecDataset  5  200 30


