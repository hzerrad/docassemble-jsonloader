from jsonloader.jsondict import JsonDict


class JsonList(list):
    """
    A subclass of list that wraps JsonDict objects
    """

    def __init__(self, jsonlist, sections):
        super().__init__(jsonlist)
        self.sections = sections

    def size(self):
        """
        returns the size (length) of the list
        :return:
        """
        return len(self)

    def filter(self, sectionSelector):
        """
        Filters the list according to the sectionSelector parameter
        :param sectionSelector: str
        :return: JsonList
        """
        filtered = []
        for record in self:
            assert isinstance(record, JsonDict)
            if record.sectionSelector == sectionSelector:
                filtered.append(record)

        return JsonList(filtered, [sectionSelector] * len(filtered))

    def __str__(self):
        string = "["
        length = len(self)

        for i in range(length):
            string += self[i].sectionSelector
            if i < length - 1:
                string += ", "
            else:
                string += "]"

        return string
