import model
import abc
from enum_class import StatusMaterialTypeEnum


class AbstractMaterialTypeServices(abc.ABC):
    @abc.abstractmethod
    def add_material_type_sv(self, request):
        pass

    @abc.abstractmethod
    def get_material_type_sv(self, request):
        pass


class MaterialTypeServices(AbstractMaterialTypeServices):
    def __init__(self, material_type_rp):
        self.material_type_rp = material_type_rp

    def add_material_type_sv(self, request):
        data = request.json
        material_type = model.MaterialTypeModel(0, data["name"], data["status"])
        try:
            self.material_type_rp.add_material_type(material_type)
        except:
            return False, "Internal Error: Execute Error"

        return True, "Success"

    def get_material_type_sv(self, request):
        name_filter = request.args.get("name")
        status_filter = request.args.get("status")
        body_filter = {}
        if name_filter is not None and len(name_filter) > 0:
            body_filter["name"] = name_filter
        if status_filter is not None and status_filter > 0:
            body_filter["status"] = status_filter

        try:
            data_material_type = self.material_type_rp.get_material_type(body_filter)
            result = []
            for item in data_material_type:
                item.status = StatusMaterialTypeEnum(item.status).name
                result.append(item.get_dict())
            return True, result
        except:
            return False, "Internal Error: Execute Error"
