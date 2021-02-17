class FoodMaterialModel(object):
    def __init__(self, id, material_id, food_id, quantity, unit):
        self.id = id
        self.material_id = material_id
        self.food_id = food_id
        self.quantity = quantity
        self.unit = unit

    def get_dict(self):
        return self.__dict__
