import os

import sys

from entry import Entry
from entry import parse_entry


class CompositeEntry(Entry):
    __slots__ = ('entries',)

    def __init__(self, path_list):
        self.entries = []
        for path in path_list.split(os.pathsep):
            self.entries.append(parse_entry(path))

    def string(self):
        _str = ''
        for e in self.entries:
            _str += e.string()
            _str += os.pathsep

        return _str

    def read_class(self, class_name):
        for e in self.entries:
            try:
                return e.read_class(class_name)
            except FileNotFoundError:
                continue

        raise FileNotFoundError


if __name__ == '__main__':
    for i in sys.path:
        print(i)
