# -*- coding: utf-8 -*-

import unittest

from lode_runner.dataprovider import dataprovider


tests_to_run = [
    "test_data_dataprovider_1",
    "test_data_dataprovider_2",
    "test_data_dataprovider_3",
    "test_method_dataprovider_1",
    "test_method_dataprovider_2",
    "test_method_dataprovider_3",
    "test_function_dataprovider_1",
    "test_function_dataprovider_2",
    "test_function_dataprovider_3",
    "test_unicode_string_dataprovider_Первый Тест",
    u"test_unicode_string_dataprovider_Второй Тест",
    "test_class_dataprovider_1",
    "test_class_dataprovider_2",
    "test_class_dataprovider_3",
    "test_dict_dataprovider['первый тест', u'второй тест']",
    "test_list_dataprovider{'one': 'первый тест', 'two': u'второй тест'}",
    "test_tuple_dataprovider('первый тест', u'второй тест')",
]


def function_provider():
    return [1, 2, 3]


class DataproviderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.set_up_class_called = True

    def setUp(self):
        self.set_up_called = True

    @dataprovider([1, 2, 3])
    def test_data_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_data_dataprovider", data))

    @property
    def value(self):
        return 1

    def method_provider(self):
        value = self.value
        return [(x + value) for x in (0, 1, 2)]

    @dataprovider(method_provider)
    def test_method_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_method_dataprovider", data))

    @dataprovider(function_provider)
    def test_function_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_function_dataprovider", data))

    @dataprovider(['Первый Тест', u"Второй Тест"])
    def test_unicode_string_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_unicode_string_dataprovider", data))

    @dataprovider([u"Первый тест"])
    def test_failed_test_with_unicode_string_in_dataprovider(self, data):
        self.assertEqual(u"test_unicode_string_dataprovider_первый тест", u"test_unicode_string_dataprovider_" + data)

    @dataprovider([['первый тест', u'второй тест']])
    def test_list_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_mixed_data_type_dataprovider", data))

    @dataprovider([{'one': 'первый тест', 'two': u'второй тест'}])
    def test_dict_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_mixed_data_type_dataprovider", data))

    @dataprovider([('первый тест', u'второй тест')])
    def test_tuple_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_mixed_data_type_dataprovider", data))

    @dataprovider([1])
    def test_setup_runs(self, data):
        self.assertTrue(self.set_up_called)
        self.assertTrue(self.set_up_class_called)


@dataprovider([1, 2, 3])
class ClassDataproviderTest(unittest.TestCase):
    def test_class_dataprovider(self, data):
        tests_to_run.remove("%s_%s" % ("test_class_dataprovider", data))


class TestAllTestsRan(unittest.TestCase):
    def test_all_tests_ran(self):
        self.assertEqual([], tests_to_run)