import unittest

from jsonloader.jsonload import JsonLoader
from jsonloader.jsondict import JsonDict


class TestJsonDict(unittest.TestCase):
    myjson = JsonLoader('../res/sample.json')
    col = myjson.collections[0]

    def test_dict(self):
        self.assertIsInstance(TestJsonDict.col, JsonDict)

    def test_set_attribute(self):
        TestJsonDict.col.record = 'My record'
        self.assertEqual(TestJsonDict.col.record, 'My record')
        self.assertEqual(TestJsonDict.col['record'], 'My record')

    def test_get_attribute(self):
        self.assertEqual(TestJsonDict.col.title, TestJsonDict.col['title'])

    def test_update_attribute(self):
        real = TestJsonDict.col.title
        TestJsonDict.col.title = 'New Title'
        self.assertEqual(TestJsonDict.col.title, 'New Title')
        self.assertEqual(TestJsonDict.col['title'], 'New Title')
        TestJsonDict.col.title = real

    def test_remove_attribute(self):
        TestJsonDict.col.record = 'My record'
        del TestJsonDict.col.record
        with self.assertRaises(KeyError):
            print(TestJsonDict.col['record'])

        with self.assertRaises(AttributeError):
            print(TestJsonDict.col.record)

        TestJsonDict.col.record = 'My Record'
        del TestJsonDict.col['record']
        with self.assertRaises(KeyError):
            print(TestJsonDict.col['record'])

        with self.assertRaises(AttributeError):
            print(TestJsonDict.col.record)

