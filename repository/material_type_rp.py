from datetime import date
import abc
import model
import array


class AbstractMaterialTypeRepository(abc.ABC):
    @abc.abstractmethod
    def add_material_type(self, material):
        pass

    @abc.abstractmethod
    def get_material_type(self, data):
        pass


class MaterialTypeRepository(AbstractMaterialTypeRepository):
    def __init__(self, pg_db):
        self.pg_db = pg_db

    def add_material_type(self, material_type):
        sql_command = "INSERT INTO public.\"MaterialType\"" \
                      "(name, status, created_date, updated_date)" \
                      "VALUES ('{}', {}, '{}', '{}');".format(material_type.name,
                                                              material_type.status,
                                                              date.today(),
                                                              date.today())

        cursor = self.pg_db.cursor()
        cursor.execute(sql_command)
        self.pg_db.commit()
        cursor.close()

    def get_material_type(self, data):
        sql_condition_arr = ["1=1"]
        if "name" in data:
            sql_condition_arr.append("name =like '%{}%'".format(data["name"]))
        if "status" in data:
            sql_condition_arr.append("status = {}".format(data["status"]))
        sql_query = "select id,name,status from public.\"MaterialType\" where {} limit 100".format(
            " and ".join(sql_condition_arr))

        cursor = self.pg_db.cursor()
        cursor.execute(sql_query)
        record = cursor.fetchall()
        cursor.close()
        list_material_type = []
        for item in record:
            material_type = model.MaterialTypeModel(item["id"], item["name"], item["status"])
            list_material_type.append(material_type)

        return list_material_type
