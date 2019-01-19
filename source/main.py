import json
import logging
import os

import sys

from ftp_downloader import FtpDownloader


def run(local_path, config_file=None):
    if config_file is None:
        config_file = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_file, "r") as f:
        config_dict = json.loads(f.read())

    downloader = FtpDownloader.load_from_config(config_dict)
    downloader(local_path=local_path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download files from ftp location')

    parser.add_argument('localpath', help="The local directory to save the files to")

    parser.add_argument('--config-file', default=None, help="A config file to use")

    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Start process
    logger.info("Starting run with arguments...\n{}".format(args.__dict__))

    run(args.localpath, args.config_file)
