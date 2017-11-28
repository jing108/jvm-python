import os

from classpath.entry import Entry
from classpath.entry_zip import ZipEntry


class WildcardEntry(Entry):
    __slots__ = ('entries',)

    def __init__(self, path):
        self.entries = []
        base_path = path[:-1]
        for p in os.listdir(base_path):
            if os.path.isfile(base_path + p) and p.endswith('.jar'):
                self.entries.append(ZipEntry(base_path + p))

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
    wildcard = WildcardEntry('/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre/lib/*')
    print(wildcard.string())
    print('\n')
    print(wildcard.read_class('java/lang/Object.class'))
