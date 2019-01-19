import tempfile
from logging.config import fileConfig
from unittest import TestCase

import os

from main import run


class ITTestMain(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), "logger.ini"))

    def test_run(self):
        local_path = tempfile.mkdtemp()
        config_file = os.path.join(os.path.dirname(__file__), "config.json")

        # Act
        run(local_path=local_path, config_file=config_file)
