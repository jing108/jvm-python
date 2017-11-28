class Classpath(object):
    __slots__ = ('bootClasspath', 'extClasspath', 'userClasspath')

    def parse(self, jreOption, cpOption):
        pass

    def read_class(self, class_name):
        class_name += '.class'

    def string(self):
        pass
