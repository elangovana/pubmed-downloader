[![Build Status](https://travis-ci.org/elangovana/pubmed-downloader.svg?branch=master)](https://travis-ci.org/elangovana/pubmed-downloader)


# Pubmed downloader
Downloads the entire pubmed abstracts as in from pubmed using FTP as detailed in https://www.nlm.nih.gov/databases/download/pubmed_medline.html


## Pre-requisites
1. Python 3.5


## How to run
1. This is an example on how to run on OSX, Unix, Linux machines. This downloads file using the config [tests/config.json](tests/config.json) and saves them to ./tmp
    ```bash
    export PYTHONPATH="./source"
    mkdir -p ./tmp
    python ./source/main.py ./tmp --config-file ./tests/config.json 
    ```
