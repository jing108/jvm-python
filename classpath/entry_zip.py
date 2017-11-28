import os
import zipfile

from classpath.entry import Entry


class ZipEntry(Entry):
    __slots__ = ('abs_path', 'jar_file')

    def __init__(self, path):
        self.abs_path = os.path.abspath(path)
        self.jar_file = None

    def string(self):
        return self.abs_path

    def read_class(self, class_name):
        if not self.jar_file:
            self.jar_file = zipfile.ZipFile(self.abs_path)

        if class_name in self.jar_file.namelist():
            return self.jar_file.read(class_name)
        else:
            raise FileNotFoundError


if __name__ == '__main__':
    _zip = ZipEntry('/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre/lib/rt.jar')
    print(_zip.read_class('java/lang/Object.class'))
