import tempfile
from logging.config import fileConfig
from unittest import TestCase

import os
from unittest.mock import Mock

from ftp_downloader import FtpDownloader


class TestFtpDownloader(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), "logger.ini"))

    def test___call__(self):
        # Arrange
        temp_local_dir = tempfile.mkdtemp()
        expected_files_len = 2

        # set up mock
        mock_ftp_client = Mock()
        mock_ftp_client.nlst.return_value = ["abc.xml", "pubmed19n049.xml", "pubmed19n041.xml", "pubmed19n041.xml.gz"]

        sut = FtpDownloader("ftp.ncbi.nlm.nih.gov", "/pubmed/baseline/", reg_ex="pubmed19n04.\.xml$")
        sut.ftp_client = mock_ftp_client

        # Act
        actual = sut(temp_local_dir)

        # Assert
        self.assertEqual(len(actual), expected_files_len)
