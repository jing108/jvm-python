import os

import sys

from classpath.entry import parse_entry
from classpath.entry_wildcard import WildcardEntry


class Classpath(object):
    __slots__ = ('boot_classpath', 'ext_classpath', 'user_classpath')

    def __init__(self, jre_option, cp_option):
        self.boot_classpath = None
        self.ext_classpath = None
        self.user_classpath = None

        self.__parse_boot_and_ext_classpath(jre_option)
        self.__parse_user_classpath(cp_option)

    def __parse_user_classpath(self, cp_option):
        if not cp_option:
            cp_option = '.'

        self.user_classpath = parse_entry(cp_option)

    def __parse_boot_and_ext_classpath(self, jre_option):
        jre_path = self.__get_jre_dir(jre_option)

        jre_lib_path = os.path.join(jre_path, 'lib', '*')
        self.boot_classpath = WildcardEntry(jre_lib_path)

        jre_ext_path = os.path.join(jre_path, 'lib', 'ext', '*')
        self.ext_classpath = WildcardEntry(jre_ext_path)

    @staticmethod
    def __get_jre_dir(jre_option):
        if jre_option and os.path.exists(jre_option):
            return jre_option

        if os.path.exists('./jre'):
            return './jre'

        home = os.environ.get('JAVA_HOME', '')

        if home:
            return os.path.join(home, 'jre')

        raise FileNotFoundError('can not find jre folder!')

    def read_class(self, class_name):
        class_name += '.class'
        try:
            return self.boot_classpath.read_class(class_name)
        except FileNotFoundError:
            try:
                return self.ext_classpath.read_class(class_name)
            except FileNotFoundError:
                try:
                    return self.user_classpath.read_class(class_name)
                except FileNotFoundError:
                    raise FileNotFoundError('class not found')

    def string(self):
        return self.user_classpath.string()


if __name__ == '__main__':
    for i in sys.path:
        print(i)
