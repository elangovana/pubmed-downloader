import glob
import tempfile
from logging.config import fileConfig
from unittest import TestCase, mock
from unittest.mock import Mock

import os
from ddt import ddt, data, unpack

from awsS3Io import AwsS3Io

"""
This is a unit test that mocks boto3 client
"""


@ddt
class TestAwsS3Io(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), "logger.ini"))

    @mock.patch('glob.glob', mock.Mock())
    @unpack
    def test_uploadfiles(self):
        # Arrange
        sut = AwsS3Io()
        mocks3client = Mock()
        sut.client = mocks3client
        glob.glob.return_value = (f for f in ["testfile", "test2.txt"])
        local_dir = tempfile.mkdtemp()

        # Act
        sut.uploadfiles(local_dir, "s3://mockbucket/path/")



    @data(("mydummyfile", "s3://mockbucket/path", "mockbucket", "path")
        , ("/user/mydummyfile", "s3://mockbucket/path/", "mockbucket", "path/mydummyfile"))
    @unpack
    def test_uploadfile(self, localfile, s3, expected_bucket, expected_key):
        # Arrange
        sut = AwsS3Io()
        mocks3client = Mock()
        sut.client = mocks3client

        # Act
        sut.uploadfile(localfile, s3)

        # Assert s3 client  was called
        mocks3client.upload_file.assert_called_with(localfile, expected_bucket, expected_key)
