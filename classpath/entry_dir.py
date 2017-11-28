import os

from classpath.entry import Entry


class DirEntry(Entry):
    __slots__ = 'abs_dir'

    def __init__(self, path):
        self.abs_dir = os.path.abspath(path)

    def string(self):
        return self.abs_dir

    def read_class(self, class_name):
        file_name = os.path.join(self.abs_dir, class_name)
        with open(file_name, 'rb') as f:
            return f.read()


if __name__ == '__main__':
    _dir = DirEntry('/Users/wands/IdeaProjects/Algorithm/src/')
    print(_dir.string())
    print(_dir.read_class('Test.class'))
