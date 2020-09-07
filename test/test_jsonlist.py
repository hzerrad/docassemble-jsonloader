import unittest
from jsonloader.jsonload import JsonLoader
from jsonloader.jsonlist import JsonList


class TestJsonList(unittest.TestCase):
    myjson = JsonLoader('../res/sample.json')

    collections = myjson.collections

    def test_type(self):
        self.assertIsInstance(TestJsonList.collections, JsonList)

    def test_filter(self):
        keyword = 'evidence'
        filtered = TestJsonList.collections.filter(keyword)
        for section in filtered.sections:
            self.assertEqual(keyword, section)
