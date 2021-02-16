from datetime import date


class MaterialRepository(object):
    def __init__(self, pg_db):
        self.pg_db = pg_db

    def add_material(self, material):
        sql_command = "INSERT INTO public.\"Material\"" \
                      "(name, status, created_date, updated_date, quantity, unit, description, material_type, image)" \
                      "VALUES ('{}', {}, '{}', '{}', {}, '{}', '{}', {}, '{}');".format(material.name,
                                                                                    material.status,
                                                                                    date.today(),
                                                                                    date.today(),
                                                                                    material.quantity,
                                                                                    material.unit,
                                                                                    material.description,
                                                                                    material.material_type,
                                                                                    material.image)
        cursor = self.pg_db.cursor()
        cursor.execute(sql_command)
        self.pg_db.commit()
        cursor.close()
