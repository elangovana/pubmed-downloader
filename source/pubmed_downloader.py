import logging
from ftplib import FTP
import re
import os

"""
Downloads the files from Pubmed
"""


class PubmedDownloader:

    def __init__(self, host, user_id=None, pwd=None):
        self.pwd = pwd
        self.user_id = user_id
        self.host = host
        self.ftp_client = None

    @property
    def logger(self):
        return logging.getLogger(__name__)

    @property
    def ftp_client(self):
        self.__ftp_client__ = self.__ftp_client__ or FTP(self.host)
        return self.__ftp_client__

    @ftp_client.setter
    def ftp_client(self, value):
        self.__ftp_client__ = value

    @staticmethod
    def load_from_config(config_dict):
        url = config_dict[__name__]["host"]
        user_id = config_dict[__name__].get("user_id", None)
        pwd = config_dict[__name__].get("pwd", None)

        return PubmedDownloader(url, user_id, pwd)

    def __call__(self, ftp_path, local_path, reg_ex=".*"):
        ftp = None
        re_obj = re.compile(reg_ex)
        result = []
        try:
            ftp = self.ftp_client
            # login
            if self.user_id is None:
                ftp.login()
            else:
                ftp.login(self.user_id, self.pwd)

            ftp.cwd(ftp_path)
            file_names = ftp.nlst()

            for filename in filter(lambda f: re_obj.match(f) is not None, file_names):
                self.logger.info("Downloading {} ..".format(filename))
                result.append(self._download_file(ftp, filename, local_path))

        finally:
            if ftp is not None: ftp.quit()
        return result

    @staticmethod
    def _download_file(ftp_connection, remote_file, local_path):
        local_filename = os.path.join(local_path, remote_file)
        with open(local_filename, 'wb') as f:
            ftp_connection.retrbinary('RETR ' + remote_file, f.write)

        return local_filename
