class Food(object):
    def __init__(self, id, name, type_food, price, status, order_total, rate, unit):
        self.id = id
        self.name = name
        self.type_food = type_food
        self.price = price
        self.status = status
        self.rate = rate
        self.order_total = order_total
        self.unit = unit

    def get_dict(self):
        return self.__dict__
