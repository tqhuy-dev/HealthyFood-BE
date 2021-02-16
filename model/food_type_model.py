class FoodTypeModel(object):
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def get_dict(self):
        return self.__dict__
