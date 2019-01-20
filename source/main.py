import json
import logging
import os

import sys

from abstract_extractor import AbstractExtractor
from awsS3Io import AwsS3Io
from ftp_downloader import FtpDownloader
from ftp_downloader_post_process import FtpDownloaderPostProcess

import gzip
import shutil


def run(local_path, config_file=None, config_str=None, s3uri=None):
    if config_str is None:
        # If no config str provided, load from file or default
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), "config.json")

        with open(config_file, "r") as f:
            config_str = f.read()

    config_dict = json.loads(config_str)

    downloader_ftp = FtpDownloader.load_from_config(config_dict)
    # Wrap the downloader_ftp with a post processing decorater to upload to s3
    downloader = FtpDownloaderPostProcess(downloader_ftp, lambda x: post_processor(x, s3uri), config_dict=config_dict)

    list(downloader.iterate(local_path=local_path))


def upload(f, s3uri):
    if s3uri is None: return
    # Upload to s3 and remove local copy
    s3io = AwsS3Io()
    s3io.uploadfile(f, s3uri)


def post_processor(f, s3uri):
    logger = logging.getLogger(__name__)
    # Run post processing
    json_file = json_extract(f)
    upload(json_file, s3uri)
    # Clean up
    logger.info("Uploaded to s3 and deleted local copy..{}".format(json_file))
    os.remove(f)
    os.remove(json_file)


def json_extract(f):
    json_file = os.path.join(os.path.dirname(f), "{}.json".format(os.path.basename(f).split(".")[0]))
    extractor = AbstractExtractor()
    with gzip.open(f, 'rb') as f_in:
        tmp_file = "{}.tmp".format(f)
        with open(tmp_file, 'wb+') as f_out:
            shutil.copyfileobj(f_in, f_out)
            f_out.seek(0)
            extractor.dump_to_file(f_out, json_file)
        os.remove(tmp_file)
    return json_file


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download files from ftp location')

    parser.add_argument('outputdir', help="The local directory to save the files to")

    parser.add_argument('--file-config', default=None, help="A config file to use")

    parser.add_argument('--json-config', default=None, help='A config file to use')

    parser.add_argument('--s3uri', default=None,
                        help="The s3 destination to upload the file to, e.g s3://mybucket/myprefix")

    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Start process
    logger.info("Starting run with arguments...\n{}".format(args.__dict__))

    run(args.outputdir, args.file_config, args.json_config, args.s3uri)
