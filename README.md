[![Build Status](https://travis-ci.org/elangovana/pubmed-downloader.svg?branch=master)](https://travis-ci.org/elangovana/pubmed-downloader)


# Pubmed downloader
Downloads the entire pubmed abstracts as in from pubmed using FTP as detailed in https://www.nlm.nih.gov/databases/download/pubmed_medline.html


## Pre-requisites
1. Python 3.5

2. Python Virtual environment setup. This is an example for python in OSX
    ```bash
    python -m pip install --user virtualenv
    mkdir ~/virtualenvironment
    python -m virtualenv  ~/virtualenvironment/pubmeddownloader
    source ~/virtualenvironment/pubmeddownloader/bin/activate
    ```
    
# Set up
1. Install dependencies within your virtual environment
    ```bash
    pip install -r source/requirements.txt
    ```

## How to run locally
** These examples on how to run on OSX, Unix, Linux machines **

1. This downloads file using the config [tests/config.json](tests/config.json) and saves them to ./tmp
    ```bash
    export PYTHONPATH="./source"
    mkdir -p ./tmp
    python ./source/main.py ./tmp --file-config ./tests/config.json 
 
    ```
    
1. This downloads file using the config passed in as arg and saves them to ./tmp
    ```bash
    export PYTHONPATH="./source"
    mkdir -p ./tmp
 
    python ./source/main.py ./tmp --json-config '{"FtpDownloader": {  "host": "ftp.ncbi.nlm.nih.gov","reg_ex": "pubmed19n0499\\.xml\\.gz$","ftp_path":"/pubmed/baseline/"}}'
    
    ```
 
1. This downloads file using the config passed in as arg and saves and upload to s3 s3://mybucket/prefix
    ```bash
    export PYTHONPATH="./source"
    mkdir -p ./tmp
 
    python ./source/main.py ./tmp --s3uri "s3://mybucket/prefix" --json-config '{"FtpDownloader": {  "host": "ftp.ncbi.nlm.nih.gov","reg_ex": "pubmed19n0499\\.xml\\.gz$","ftp_path":"/pubmed/baseline/"},  "FtpDownloaderPostProcess": { "num_workers": 2 }}'
    ```

## Run on docker

```bash
docker run -v /tmp:/data lanax/pubmed-downloader main.py "/data" --s3uri "s3://mybucket/prefix" --json-config '{"FtpDownloader": {  "host": "ftp.ncbi.nlm.nih.gov","reg_ex": "pubmed19n0499\\.xml\\.gz$","ftp_path":"/pubmed/baseline/"}, "FtpDownloaderPostProcess": { "num_workers": 2 }}'
```