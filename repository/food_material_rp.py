import model
import abc


class AbstractFoodMaterialRepository(abc.ABC):
    @abc.abstractmethod
    def add_food_material(self, food_material):
        pass

    @abc.abstractmethod
    def get_food_material(self, food_id):
        pass


class FoodMaterialRepository(AbstractFoodMaterialRepository):
    def __init__(self, pg_db):
        self.pg_db = pg_db

    def add_food_material(self, food_material):

        sql_command_item = []
        for item in food_material:
            sql_command_item.append(f"({item.food_id}, {item.material_id}, {item.quantity}, '{item.unit}')")

        sql_command_all = "INSERT INTO public.\"FoodMaterial\"" \
                          "(food_id, material_id, quantity, unit) " \
                          "VALUES {}".format(",".join(sql_command_item))
        cursor = self.pg_db.cursor()
        cursor.execute(sql_command_all)
        self.pg_db.commit()
        cursor.close()

    def get_food_material(self, food_id):
        pass
