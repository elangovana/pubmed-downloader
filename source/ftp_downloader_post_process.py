import logging

from queue import Queue
from threading import Thread

"""
Post processing decorater logic for FtpDownloader
"""


class FtpDownloaderPostProcess:

    def __init__(self, ftp_downloader, post_processor):
        self.post_processor = post_processor
        self.ftp_downloader = ftp_downloader

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def iterate(self, *args, **kwargs):
        """
Uses worker queues to perform the postprocessing
        :param args:
        :param kwargs:
        """
        # use thread pool to parallel process
        q = Queue()
        t = Thread(target=lambda: self._worker(q))
        t.start()

        for f in self.ftp_downloader.iterate(*args, **kwargs):
            q.put(f)
            yield f
        # poison pill
        q.put(None)
        t.join()

    def _worker(self, read_queue):
        while True:
            item = read_queue.get()
            if item is None:
                return
            self.post_processor(item)

    def __call__(self, *args, **kwargs):
        items = self.ftp_downloader(*args, **kwargs)
        for item in items:
            self.post_processor(item)
        return items
