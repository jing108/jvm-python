class Entry(object):
    def read_class(self, class_name):
        raise NotImplementedError

    def string(self):
        raise NotImplementedError

    def new_entry(self, path):
        pass
