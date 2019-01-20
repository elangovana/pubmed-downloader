from unittest import TestCase
from unittest.mock import Mock
import timeout_decorator

from ftp_downloader_post_process import FtpDownloaderPostProcess


class TestFtpDownloaderPostProcess(TestCase):

    @timeout_decorator.timeout(2, exception_message="The function should exit on error, but instead hangs.. ")
    def test_iterate_should_not_hang_when_main_fails(self):
        """
        Should not hang when the main called function fails
        """

        # Arrange
        mock_downloader = Mock()
        mock_post_processor = Mock()

        # Throw error in the iterator
        mock_downloader.iterate.side_effect = lambda: 1 / 0
        sut = FtpDownloaderPostProcess(mock_downloader, mock_post_processor)

        # Act
        with self.assertRaises(ZeroDivisionError):
            list(sut.iterate())

    def test_iterate_should_not_hang_when_worker_fails(self):
        """
        Should not hang when the workers fail and the error faced by workers bubbles up
        """

        # Arrange
        mock_downloader = Mock()
        mock_post_processor = Mock()

        # Throw error in the post processor
        mock_post_processor.side_effect = lambda x: 1 / 0
        mock_downloader.iterate.return_value = [1, 1]
        sut = FtpDownloaderPostProcess(mock_downloader, mock_post_processor)

        # Act
        with self.assertRaises(ZeroDivisionError):
            list(sut.iterate())
