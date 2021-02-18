from datetime import date
import abc
from model import MaterialModel


class AbstractMaterialRepository(abc.ABC):

    @abc.abstractmethod
    def add_material(self, material):
        pass

    @abc.abstractmethod
    def get_material(self, data):
        pass

    @abc.abstractmethod
    def add_material_by_list(self, list_material):
        pass


class MaterialRepository(AbstractMaterialRepository):
    def __init__(self, pg_db):
        self.pg_db = pg_db

    def add_material(self, material):
        sql_command = "INSERT INTO public.\"Material\"" \
                      "(name, status, created_date, updated_date, quantity, unit, " \
                      "description, material_type, image , price)" \
                      f"VALUES ('{material.name}', {material.status}, '{date.today()}', '{date.today()}'" \
                      f", {material.quantity}, '{material.unit}', " \
                      f"'{material.description}', {material.material_type}, '{material.image}' , {material.price});"
        cursor = self.pg_db.cursor()
        cursor.execute(sql_command)
        self.pg_db.commit()
        cursor.close()

    def get_material(self, data):
        sql_condition = ["1=1"]
        if "name" in data:
            sql_condition.append("name like '%{}%'".format(data["name"]))
        if "status" in data:
            sql_condition.append("status = {}".format(data["status"]))
        if "material_type" in data:
            sql_condition.append("material_type = {}".format(data["material_type"]))

        sql_query = "select id,name,status,quantity,unit,description,material_type,image,price " \
                    "from public.\"Material\" where {} limit 100".format(" and ".join(sql_condition))

        cursor = self.pg_db.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()
        list_material = []

        for item in records:
            material = MaterialModel(item["id"],
                                     item["name"],
                                     item["status"],
                                     item["quantity"],
                                     item["unit"],
                                     item["description"],
                                     item["material_type"],
                                     item["image"],
                                     float(item["price"]))

            list_material.append(material)
        cursor.close()
        return list_material

    def add_material_by_list(self, list_material):
        sql_command_arr = []
        for material in list_material:
            sql_command_arr.append(f"('{material.name}', {material.status}, '{date.today()}', '{date.today()}'" \
                                   f", {material.quantity}, '{material.unit}', " \
                                   f"'{material.description}', {material.material_type}, "
                                   f"'{material.image}' , {material.price})")

        sql_command = "INSERT INTO public.\"Material\"" \
                      "(name, status, created_date, updated_date, quantity, unit, " \
                      "description, material_type, image , price)" \
                      "VALUES {}".format(",".join(sql_command_arr))

        cursor = self.pg_db.cursor()
        cursor.execute(sql_command)
        self.pg_db.commit()
        cursor.close()
