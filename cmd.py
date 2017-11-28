import argparse

import sys


class Cmd(object):
    __slots__ = ('cp_option', 'class_name', 'args', 'jre_option')

    def __init__(self, argv):
        parser = argparse.ArgumentParser(description='jvm by wands')

        parser.add_argument('-v', '--version', action='version', version='1.0.0')
        parser.add_argument('class_info', nargs='+')
        parser.add_argument('-cp', '--classpath', help='classpath')
        parser.add_argument('-Xjre', help='jre dir')

        _argv = parser.parse_args(argv)

        self.jre_option = _argv.Xjre
        self.cp_option = _argv.classpath
        if len(_argv.class_info) > 1:
            self.class_name = _argv.class_info[0]
            self.args = _argv.class_info[1:]

    def print_info(self):
        print("classpath:%s class:%s args:%s" % (self.cp_option, self.class_name, self.args))


if __name__ == '__main__':
    cmd = Cmd(sys.argv[1:])
    cmd.print_info()
