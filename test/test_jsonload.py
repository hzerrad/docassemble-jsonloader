import unittest
import orjson
import os

from jsonloader.jsonload import JsonLoader


class TestJsonLoader(unittest.TestCase):
    FILEPATH = '../res/sample.json'

    def test_load_path(self):
        JsonLoader(TestJsonLoader.FILEPATH)

    def test_load_file(self):
        with open(TestJsonLoader.FILEPATH, 'r') as FILE:
            JsonLoader(FILE)

    def test_load_text(self):
        FULLJSON = None
        with open(TestJsonLoader.FILEPATH, 'r') as FILE:
            FULLJSON = orjson.dumps(orjson.loads(FILE.read()))

        self.assertIsNotNone(FULLJSON, "orjson did not load file.")
        JsonLoader(FULLJSON)

    myjson = JsonLoader(FILEPATH)

    def test_get_raw_object(self):
        self.assertIs(TestJsonLoader.myjson.get_raw_object(), dict)

    def test_get_raw_json(self):
        self.assertTrue(isinstance(TestJsonLoader.myjson.get_raw_json(), str))
        self.assertTrue(isinstance(TestJsonLoader.myjson.get_raw_json(False), bytes))

    def test_attributes(self):
        self.assertTrue("__origin" not in TestJsonLoader.myjson.get_attributes())
        self.assertEqual(len(TestJsonLoader.myjson.get_attributes()), 4)

    def test_dump(self):
        savepath = "newsample.json"
        TestJsonLoader.myjson.dump(savepath)
        self.assertTrue(os.path.exists(savepath))
        os.remove(savepath)

        farsavepath = "../res/newsample"
        TestJsonLoader.myjson.dump(farsavepath)
        self.assertTrue(os.path.exists(farsavepath+".json"))
        os.remove(farsavepath+".json")