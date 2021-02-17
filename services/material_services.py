import model
import abc
from enum_class import StatusMaterialTypeEnum


class AbstractMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_material(self, request):
        pass


class MaterialServices(AbstractMaterialServices):
    def __init__(self, material_rp):
        self.material_rp = material_rp
        self.material_type_rp = None

    def set_material_type_rp(self, material_type_rp):
        self.material_type_rp = material_type_rp

    def add_material(self, request):
        data = request.json
        body_material_type_filter = {
            "status": StatusMaterialTypeEnum.Available.value
        }
        try:
            material_type_data = self.material_type_rp.get_material_type(body_material_type_filter)

            def get_value_mt(mt):
                return mt.id

            mt_arr_id = list(map(get_value_mt, material_type_data))

            if data["material_type"] not in mt_arr_id:
                return False, "Bad Request: Material Type Id Is Invalid"

            material = model.MaterialModel(0,
                                           data["name"],
                                           data["status"],
                                           data["quantity"],
                                           data["unit"],
                                           data["description"],
                                           data["material_type"],
                                           ",".join(data["image"]))

            self.material_rp.add_material(material)
        except:
            return False, "Internal Error:Execute Error"
        return True, "Success"
