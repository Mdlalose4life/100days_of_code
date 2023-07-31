#!/usr/bin/env python

from systems import rm
import os.path
import unittest

class RmTest(unittest.TestCase):
    tempfilepath = os.path(tempfile.gettempdir(), "tmo-testfile")

    def setUp(self):
        with open(self.tempfilepath, "ws") as f:
            f.write("Delete me!")

    def test_rm(self):
        rm(self.tempfilepath)
        self.assertFalse(os.path.isfile(self.tmpfile), "Failed to remove the file")