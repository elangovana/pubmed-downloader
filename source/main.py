import json
import os

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

    parser.add_argument('--regex', help="The regular expression to file", default=".*")

    parser.add_argument('--config-file', default=None, help="A config file to use")
