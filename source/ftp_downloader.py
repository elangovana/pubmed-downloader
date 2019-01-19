import logging
from ftplib import FTP
import re
import os

"""
Downloads the files through FTP
"""


class FtpDownloader:

    def __init__(self, host, ftp_path, user_id=None, pwd=None, reg_ex=".*"):
        self.ftp_path = ftp_path
        self.reg_ex = reg_ex
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
        cls_name = "FtpDownloader"
        url = config_dict[cls_name]["host"]
        ftp_path = config_dict[cls_name]["ftp_path"]
        user_id = config_dict[cls_name].get("user_id", None)
        pwd = config_dict[cls_name].get("pwd", None)
        reg_ex = config_dict[cls_name].get("reg_ex", ".*")
        return FtpDownloader(url, ftp_path, user_id, pwd, reg_ex)

    def iterate(self, local_path):
        ftp = None
        re_obj = re.compile(self.reg_ex)
        # Make the local path and ignore if exists..
        os.makedirs(local_path, exist_ok=True)
        try:
            ftp = self.ftp_client
            # login
            if self.user_id is None:
                ftp.login()
            else:
                ftp.login(self.user_id, self.pwd)

            ftp.cwd(self.ftp_path)
            file_names = ftp.nlst()

            for filename in filter(lambda f: re_obj.match(f) is not None, file_names):
                self.logger.info("Downloading {} ..".format(filename))
                yield self._download_file(ftp, filename, local_path)


        finally:
            if ftp is not None: ftp.quit()

    def __call__(self, local_path):
        return list(self.iterate(local_path))

    @staticmethod
    def _download_file(ftp_connection, remote_file, local_path):
        local_filename = os.path.join(local_path, remote_file)
        with open(local_filename, 'wb') as f:
            ftp_connection.retrbinary('RETR ' + remote_file, f.write)

        return local_filename
