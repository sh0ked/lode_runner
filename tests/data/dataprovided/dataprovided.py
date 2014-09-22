# coding: utf-8

import unittest
from lode_runner.dataprovider import dataprovider


class ChildTestCase(unittest.TestCase):
    pass


class TestFixtureCase(ChildTestCase):
    @dataprovider([1, 2, 3])
    def test_with_dataprovider_FIXTURE(self, data):
        pass
