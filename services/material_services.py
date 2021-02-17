import model
import abc
from enum_class import StatusMaterialTypeEnum


class AbstractMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_material_sv(self, request):
        pass

    @abc.abstractmethod
    def get_material_sv(self, request):
        pass


class MaterialServices(AbstractMaterialServices):
    def __init__(self, material_rp):
        self.material_rp = material_rp
        self.material_type_rp = None

    def set_material_type_rp(self, material_type_rp):
        self.material_type_rp = material_type_rp

    def add_material_sv(self, request):
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
                                           ",".join(data["image"]),
                                           data["price"])

            self.material_rp.add_material(material)
        except:
            return False, "Internal Error:Execute Error"
        return True, "Success"

    def get_material_sv(self, request):
        try:
            name_arg = request.args.get("name")
            status_arg = request.args.get("status")
            material_type_arg = request.args.get("material_type")
            body_filter = {}
            if name_arg is not None and len(name_arg) > 0:
                body_filter["name"] = name_arg
            if status_arg is not None and int(status_arg) > 0:
                body_filter["status"] = int(status_arg)
            if material_type_arg is not None and int(material_type_arg) > 0:
                body_filter["material_type"] = int(material_type_arg)

            data_material = self.material_rp.get_material(body_filter)
            result = []
            for item in data_material:
                result.append(item.get_dict())

            return True, result
        except:
            return False, "Internal Error"
