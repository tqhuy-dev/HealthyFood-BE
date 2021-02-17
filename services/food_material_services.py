import abc
import model


class AbstractFoodMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_food_material_sv(self, request, food_id):
        pass

    @abc.abstractmethod
    def get_food_material_sv(self, food_id):
        pass


class FoodMaterialServices(AbstractFoodMaterialServices):
    def __init__(self, food_material_rp):
        self.food_material_rp = food_material_rp

    def add_food_material_sv(self, request, food_id):
        try:
            data = request.json
            list_fm = []
            for item in data:
                fm_model = model.FoodMaterialModel(0, item["material_id"], food_id, item["quantity"], item["unit"])
                list_fm.append(fm_model)
            self.food_material_rp.add_food_material(list_fm)
            return True, "Success"
        except:
            return False, "Internal Error"

    def get_food_material_sv(self, food_id):
        pass
