import os


class Entry(object):
    def read_class(self, class_name):
        raise NotImplementedError

    def string(self):
        raise NotImplementedError


def parse_entry(path):
    if isinstance(path, str):
        if os.pathsep in path:
            from .entry_composite import CompositeEntry
            return CompositeEntry(path)
        elif '*' in path:
            from .entry_wildcard import WildcardEntry
            return WildcardEntry(path)
        elif path.endswith('.jar') or path.endswith('.JAR') or path.endswith('.zip') or path.endswith('.ZIP'):
            from .entry_zip import ZipEntry
            return ZipEntry(path)
        else:
            from .entry_dir import DirEntry
            return DirEntry(path)
