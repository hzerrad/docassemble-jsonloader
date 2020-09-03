from jsonloader.jsondict import JsonDict

class JsonList(list):

    def __init__(self, jsonlist, sections):
        super().__init__(jsonlist)
        self.sections = sections

    def size(self):
        return len(self)

    def filter(self, sectionSelector):
        filtered = []
        for record in self:
            assert isinstance(record, JsonDict)
            if record.sectionSelector == sectionSelector:
                filtered.append(record)

        return JsonList(filtered, [sectionSelector] * len(filtered))