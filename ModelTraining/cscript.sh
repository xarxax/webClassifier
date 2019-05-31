#g++ gloveGenerator.cpp -o gloveGenerator -std=c++11 -O2
#g++ gloveGenerator2.cpp -o gloveGenerator2 -std=c++11 -O2
export OMP_NUM_THREADS=6
g++ gloveGenerator2OMP.cpp -o gloveGenerator2OMP -std=c++11 -fopenmp -O2
#./gloveGenerator2 <<<'1000000  glove '
./gloveGenerator2OMP <<<'1000000  glove '
