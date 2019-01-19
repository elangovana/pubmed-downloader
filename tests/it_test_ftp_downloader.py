import tempfile
from logging.config import fileConfig
from unittest import TestCase

import os

from ftp_downloader import FtpDownloader


class ITTestFtpDownloader(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), "logger.ini"))

    def test___call__(self):
        # Arrange
        sut = FtpDownloader("ftp.ncbi.nlm.nih.gov","/pubmed/baseline/", reg_ex="pubmed19n0499\.xml\.gz$")
        temp_local_dir = tempfile.mkdtemp()
        expected_files_len = 1

        # Act
        actual = sut( temp_local_dir)

        # Assert
        self.assertEqual(len(actual), expected_files_len)
