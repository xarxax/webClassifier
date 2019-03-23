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
    //and the one to the current web
    vector<string> words;
    vector<vector<float> > vectors;
    vector<string> folderNames;
    vector<vector<string> > documents;
    vector<vector<float> > documentsWE;
    string modelName,inputPath = "tokenizedDataset";

    cin >> numFiles >> modelName;
    cout << "I read " << numFiles <<  " files. Model: " <<modelName << endl;
    //Adding WE
    cout << "Loading WE..." << endl;
    ifWE.open("glove.840B.300d.txt");
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
    }
    cout << "WE Loaded." << endl << "Loading documents..." << endl;
    read_directory(inputPath,folderNames);//this loads . and .. as the first files
    documents = vector<vector<string> >(folderNames.size(),vector<string>(0));//we alloc memory and make sure they start as empty
    for(int i=2;i< folderNames.size(); ++i){//so we started at position 2
        folderNames[i]= inputPath +"/"+ folderNames[i]+"/text.txt";
        ifWebpage.open(folderNames[i]);
        //cout << folderNames[i] << endl;
        while (ifWebpage >> word)
            documents[i].push_back(word);
    }
    //cout << documents[2].size() << endl;
    cout << "Documents loaded." << endl;
    cout << "Turning documents to WE..." << endl;

    //Now we must substitute every document for its representation and write them
    documentsWE =  vector<vector<float> >(folderNames.size(),vector<float>(300,0.));
    for(int i=0;i< words.size(); ++i)//this way we guarantee that we wont have
      //to search a huge vector every time
        for(int j=0;j<folderNames.size();++j)
            for(int k=0;k<folderNames[j].size();++k){
              if(words[i] == documents[j][k])
                  sum_vectorvalue(documentsWE[j],vectors[i]);
            }


    cout << "Documents turned." << endl;


    return 0;
}
