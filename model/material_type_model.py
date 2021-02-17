class MaterialTypeModel(object):
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def get_dict(self):
        return self.__dict__
