#!/bin/sh

'''
Creates/refreshes a local directory, data, with latest chrisheet.org yaml files
'''

mkdir -p data
cd data 
rm *.yml
rm README.txt extract.zip
curl https://cricsheet.org/downloads/all.zip > extract.zip
unzip extract.zip 
cd ..