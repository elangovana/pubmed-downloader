# Register AWS batch job

## Prerequisites
1. Python 3.5+, https://www.python.org/downloads/release/python-350/ 
2. Install pip, see https://pip.pypa.io/en/stable/installing/ 

## Setup
3. Install dependencies for this project
    ```bash
    pip install -r aws_batch/requirements.txt
    ``` 
4. Make sure you have registered the docker image using the docker file [../source/Dockerfile](../source/Dockerfile)


## How to run

1. Register a aws batch job
    ```bash
    export PYTHONPATH=./aws_batch
    
    python ./source/main.py ./tmp --s3uri "s3://mybucket/pubmed-json/" --json-config '{"FtpDownloader": {  "host": "ftp.ncbi.nlm.nih.gov","reg_ex": "pubmed19n049.\\.xml\\.gz$","ftp_path":"/pubmed/baseline/"}, "FtpDownloaderPostProcess": {    "num_workers": 10 }}'

    
    #For full details
    python aws_batch/register_sample_job.py -h 

    ```

2. If you go to the AWS Batch console -- Job definition , you will see the new job called pubmed_downloader.

5. You can then trigger a new job through the AWS Batch console. Pass in the name of the s3destination as one of the parameters in the job.
