import sys

import os

from classpath.classpath import Classpath
from cmd import Cmd


def start_jvm(cmd):
    class_data = None
    cp = Classpath(cmd.jre_option, cmd.cp_option)
    print('classpath:%s class:%s args:%s\n' % (cp.string(), cmd.class_name, cmd.args))
    class_name = cmd.class_name.replace('.', '/')

    try:
        class_data = cp.read_class(class_name)
    except FileNotFoundError as e:
        print(e.filename)

    print('class data: ' + str(class_data))


if __name__ == '__main__':
    _cmd = Cmd(sys.argv[1:])
    start_jvm(_cmd)
