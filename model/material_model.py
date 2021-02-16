class MaterialModel(object):
    def __init__(self, id, name, status, quantity, unit, description, material_type, image):
        self.id = id
        self.name = name
        self.status = status
        self.quantity = quantity
        self.unit = unit
        self.description = description
        self.material_type = material_type
        self.image = image
