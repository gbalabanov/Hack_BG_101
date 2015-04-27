from requesting import GHInfo
import unittest

class TestGHInfo(unittest.TestCase):

    def setUp(self):
        g = GHInfo("dasd")

    def test_get_followers(self):

