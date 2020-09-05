from typing import Any
import json


class JsonDict:

    def __init__(self, jsondict, sectionSelector):
        assert isinstance(jsondict, dict)
        super(JsonDict, self).__setattr__('rawjson', jsondict)
        super(JsonDict, self).__setattr__('sectionSelector', sectionSelector)
        self.__slots__ = ['rawjson', 'sectionSelector'] + list(jsondict.keys())
        self.init_attr()

    def keys(self) -> list:
        l = list(self.rawjson.keys())
        l.remove('__slots__')
        return l

    def init_attr(self):
        for key in self.keys():
            super(JsonDict, self).__setattr__(key, self.rawjson[key])

    def __setattr__(self, key, value):
        if key in ['rawjson', 'sectionSelector']:
            raise AttributeError('{} is read-only'.format(key))
        super(JsonDict, self).__setattr__(key, value)
        self.rawjson[key] = value

    def __delattr__(self, item):
        if item in self.keys():
            self.__delitem__(item)
        else:
            super(JsonDict, self).__delattr__(item)

    def __setitem__(self, key, value):
        self.rawjson[key] = value
        super(JsonDict, self).__setattr__(key, value)

    def __getitem__(self, key):
        return self.rawjson[key]

    def __delitem__(self, key):
        del self.rawjson[key]
        super(JsonDict, self).__delattr__(key)

    def __str__(self):
        return json.dumps(self.rawjson, indent=4)