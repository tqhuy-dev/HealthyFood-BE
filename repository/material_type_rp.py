from datetime import date
import abc


class AbstractMaterialTypeRepository(abc.ABC):
    @abc.abstractmethod
    def add_material_type(self, material):
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
