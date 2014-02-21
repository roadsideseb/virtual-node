import sys
import logging
import subprocess

sys.path.insert(0, '..')

from unittest2 import TestCase


class MockLoggingHandler(logging.Handler):
    """Mock logging handler to check for expected logs."""

    def __init__(self, *args, **kwargs):
        self.reset()
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        self.messages[record.levelname.lower()].append(record.getMessage())

    def reset(self):
        self.messages = {
            'debug': [],
            'info': [],
            'warning': [],
            'error': [],
            'critical': [],
        }


class TestNode(TestCase):

    def test_is_installed(self):
        proc = subprocess.Popen(['node', '--version'], stdout=subprocess.PIPE)
        output = proc.stdout.read()
        self.assertEquals(output.strip(), 'v0.10.26')
