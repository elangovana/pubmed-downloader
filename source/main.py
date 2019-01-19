import json
import logging
import os

import sys

from awsS3Io import AwsS3Io
from ftp_downloader import FtpDownloader


def run(local_path, config_file=None, config_str=None, s3uri=None):
    logger = logging.getLogger(__name__)
    if config_str is None:
        # If no config str provided, load from file or default
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), "config.json")

        with open(config_file, "r") as f:
            config_str = f.read()

    config_dict = json.loads(config_str)

    downloader = FtpDownloader.load_from_config(config_dict)
    for f in downloader.iterate(local_path=local_path):
        if s3uri is not None:
            # Upload to s3 and remove local copy
            s3io = AwsS3Io()
            s3io.uploadfile(f, s3uri)
            # TODO: Use flag to have option to retain local copy
            logger.info("Uploaded to s3 and deleted local copy..{}".format(f))
            os.remove(f)


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
