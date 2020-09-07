from typing import Any
import json


class JsonDict:
    """
    A special dict wrapper that allows easy access to various subnodes of a Docassemble element.
    """
    def __init__(self, jsondict, sectionSelector):
        assert isinstance(jsondict, dict)
        super(JsonDict, self).__setattr__('rawjson', jsondict) # set rawjson attribute to the raw object
        super(JsonDict, self).__setattr__('sectionSelector', sectionSelector) # set the current sectionSelector
        self.__slots__ = ['rawjson', 'sectionSelector'] + list(jsondict.keys())

        # initializing attributes
        self.init_attr()

    def keys(self) -> list:
        """
        Gets the list of all subnodes
        :return: dict
        """
        l = list(self.rawjson.keys())
        l.remove('__slots__')
        return l

    def init_attr(self):
        """
        Initializes the object with all subnodes
        """
        for key in self.keys():
            super(JsonDict, self).__setattr__(key, self.rawjson[key]) # set key as an attribute

    def __setattr__(self, key, value):
        # rawjson and sectionSelector are read-only
        if key in ['rawjson', 'sectionSelector']:
            raise AttributeError('{} is read-only'.format(key))

        # Update the object both in the attribute and the raw json dict
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
        del self.rawjson[key] # remove key
        super(JsonDict, self).__delattr__(key) # remove attribute

    def __str__(self):
        return json.dumps(self.rawjson, indent=4)