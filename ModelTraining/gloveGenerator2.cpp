#include <iostream>
#include <vector>
#include <fstream>
#include <dirent.h>
using namespace std;


void read_directory(const string& name, vector<string>& v)
{
    DIR* dirp = opendir(name.c_str());
    struct dirent * dp;
    while ((dp = readdir(dirp)) != NULL) {
        v.push_back(dp->d_name);
    }
    closedir(dirp);
}

void sum_vectorvalue(vector<float>& base, vector<float>& added ){
  for(int i=0; i<300 ;++i){
    base[i]+=added[i];
  }
}



int main()
{
    int numFiles;//number of files to transform
    ifstream ifWE,ifWebpage;//interface to the big file
    ofstream outputDocument;
    //and the one to the current web
    vector<string> words;
    vector<vector<float> > vectors;
    vector<string> folderNames,folderNamesOutput;
    vector<vector<string> > documents;
    vector<vector<float> > documentsWE;
    vector<int> numWords;//this counts how many word vectors a document combines in its input. 
    string modelName,inputPath = "tokenizedDataset";
    string outputPath;
    int trash;

    cin >> numFiles >> modelName;
    cout << "I read " << numFiles <<  " files. Model: " <<modelName << endl;
    //Adding WE

    outputPath = modelName + "AveragedDataset";
    cout << "Loading WE..." << endl;
    if(modelName == "glove") ifWE.open("glove.840B.300d.txt");
    else if (modelName == "lexvec")  {
      ifWE.open("lexVec58Bvectors300.txt");
      ifWE >> trash;
      ifWE >> trash;//we will not be using them
    }else {
      cout << "Wrong model name. Aborting" << endl;
      return -1;
    }
    string word;
    int curr=0;
    while(ifWE >> word){
        //cout << word << endl;
        words.push_back(word);
        vectors.push_back(vector<float>(300));
        for(int i =0 ; i< 300; ++i){
            float val;
            ifWE >> val;
            vectors[curr][i]=val;
        }
        curr+=1;
        //if(curr==100000) break;
    }

    ifWE.close();
    cout << "WE Loaded." << endl << "Loading documents..." << endl;
    read_directory(inputPath,folderNames);//this loads . and .. as the first files

    cout << "Documents Loaded." << endl << "Loading output documents..." << endl;
    read_directory(outputPath,folderNamesOutput);//this loads . and .. as the first files
    cout << "Output documents Loaded." << endl << "Removing Files already processed..." << endl;

    int maxDocs=folderNames.size(), doneDocs=folderNamesOutput.size();
    int j=2,removed = 0;
    if(doneDocs > 2){
      for(int i=2;i<folderNames.size();i++){
        while(folderNamesOutput[j]== folderNames[i]){
          folderNames.erase(folderNames.begin()+i);//erase is very slow, but it this is the
          folderNamesOutput.erase(folderNamesOutput.begin()+j);
          removed++;//faster part of the execution
        }
      }
    }
    cout << "Removed Files already processed." << endl << "Loading output documents..." << endl;

    cout << "We will treat " << (maxDocs-removed-2)  << " documents. Vector has length " << (folderNames.size()-2) << endl;
    cout << "output folder has " << doneDocs  << " documents" << endl;

    //cout << folderNames[2] << endl;
    documents = vector<vector<string> >(folderNames.size(),vector<string>(0));//we alloc memory and make sure they start as empty
    for(int i=2;i< folderNames.size(); ++i){//so we started at position 2
        folderNames[i]= inputPath +"/"+ folderNames[i]+"/text.txt";
        ifWebpage.open(folderNames[i]);
        //cout << folderNames[i] << endl;
        while (ifWebpage >> word)
            //cout << word << ' ';
            documents[i].push_back(word);
        ifWebpage.close();
        //if (i==4) break;

    }

    //cout << documents[2].size() << endl;
    cout << "Documents loaded." << endl;
    cout << "Allocating memory for WE documents..." << endl;

    //Now we must substitute every document for its representation and write them
    documentsWE =  vector<vector<float> >(folderNames.size(),vector<float>(300,0.));
    cout << folderNames[0] << endl;
    //numwords has the same size as the amount of folders.
    numWords = vector<int>(folderNames.size(), 0);
    cout << "Turning documents to WE..." << endl;
    for(int i=0;i< words.size(); ++i){//this way we guarantee that we wont have
      //to search a huge vector every time
        //cout << "++++++++++++++++++++" << endl;
        cout << words[i] <<   "  " << i << endl;
        for(int j=2;j<folderNames.size();++j){//skip . and ..
            //cout << "#####################################" << endl;
            //cout << folderNames[j] << endl;
            //cout << documents[j].size() << endl;
            for(int k=0;k<documents[j].size();++k){
              //cout << "**********************************" << endl;
              //cout << documents[j][k] << endl;
              //cout << documents[j][k] << endl;
              if(words[i] == documents[j][k]){
                  //cout << "-----------------------------------" << endl;
                  //cout << documentsWE[j].size() << endl;
                  //cout << words[i]<< " colision." << endl;
                  sum_vectorvalue(documentsWE[j],vectors[i]);
                  numWords[j]++;
              }
            }
            //if (j==4) break;

        }
        //break;
    }
    cout << "Averaging vectors.." << endl;
    for(int i=2;i<folderNames.size();++i){
    	for(int j=0;j<documentsWE[i].size();++j)
    		documentsWE[i][j]= documentsWE[i][j] / float(numWords[i]);
    }
    cout << "Averaged." << endl;
    cout << "Documents turned." << endl;
    cout << "Writing WE documents..." << endl;
    for(int i=2;i< folderNames.size(); ++i){//this way we guarantee that we wont have
      //cout << folderNames[i] << endl;
      folderNames[i].replace(folderNames[i].begin(),folderNames[i].begin()+9,modelName);
      string folderWithoutText=folderNames[i];
      folderWithoutText.replace(folderWithoutText.end()-9,folderWithoutText.end(),"");
      //cout << folderNames[i] << endl;
      cout <<  folderWithoutText << endl;
      //creat folder if does not exist
      outputDocument.open(folderWithoutText);
      for(int j = 0;j< documentsWE[i].size();j++){
        outputDocument << documentsWE[i][j] << " ";
        //cout << documentsWE[i][j] << endl;
      }
      outputDocument.close();
      //if (i==4) break;
      //break;

    }
    cout << "Documents written." << endl;

    return 0;
}
