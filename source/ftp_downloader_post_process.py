import logging

from queue import Queue
import concurrent.futures

"""
Post processing decorater logic for FtpDownloader
"""


class FtpDownloaderPostProcess:

    def __init__(self, ftp_downloader, post_processor, num_workers=None, config_dict=None):
        self.post_processor = post_processor
        self.ftp_downloader = ftp_downloader
        self.num_workers = num_workers or self._get_from_config(config_dict, "num_workers", 5)

    @staticmethod
    def _get_from_config(config_dict, key, default_value):
        value = default_value
        if config_dict is not None:
            cls_name = "FtpDownloaderPostProcess"
            if config_dict.get(cls_name, None) is not None:
                value = config_dict[cls_name].get(key, 5)
        return value

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

        max_workers = self.num_workers
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Set up workers
            futures = []
            for i in range(max_workers):
                futures.append(executor.submit(self._worker, q))

            # Submit worker jobs
            # Wrap the main task in a try block so that the queue completes regardless of success/failure of main job
            try:
                for f in self.ftp_downloader.iterate(*args, **kwargs):
                    q.put(f)
                    yield f
            finally:
                # Stop processing
                # Not doing a queue to join, because if all workers fail this will hang with items still left in q...
                # q.join()

                # poison pill
                for i in range(max_workers):
                    q.put(None)
                for future in futures:
                    future.result()

    def _worker(self, read_queue):
        while True:
            item = read_queue.get()
            if item is None:
                return
            try:
                self.post_processor(item)
            except Exception as e:
                self.logger.warning("The task has failed with error ..{}".format(e))

                raise e
            read_queue.task_done()

    def __call__(self, *args, **kwargs):
        items = self.ftp_downloader(*args, **kwargs)
        for item in items:
            self.post_processor(item)
        return items
