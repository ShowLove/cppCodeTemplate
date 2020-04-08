#!/bin/bash

# from terminal copy and paste
#cd /Users/carlosgarzon/Desktop/code/cpp/codeQs/tests/build && cmake /Users/carlosgarzon/Desktop/code/cpp/codeQs && make && ./tests/gtestProject

#rm -rf /Users/carlosgarzon/Desktop/code/cpp/codeQs/tests/build
#mkdir /Users/carlosgarzon/Desktop/code/cpp/codeQs/tests/build
cd /Users/carlosgarzon/Desktop/code/cpp/codeQs/tests/build
cmake /Users/carlosgarzon/Desktop/code/cpp/codeQs
make
./tests/gtestProject
cd /Users/carlosgarzon/Desktop/code/cpp/scripts/createNewClass