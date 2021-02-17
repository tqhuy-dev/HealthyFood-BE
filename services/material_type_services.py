import model
import abc


class AbstractMaterialTypeServices(abc.ABC):
    @abc.abstractmethod
    def add_material_type_sv(self, request):
        pass


class MaterialTypeServices(AbstractMaterialTypeServices):
    def __init__(self, material_rp):
        self.material_rp = material_rp

    def add_material_type_sv(self, request):
        data = request.json
        material_type = model.MaterialTypeModel(0, data["name"], data["status"])
        try:
            self.material_rp.add_material_type(material_type)
        except:
            return False, "Internal Error: Execute Error"

        return True, "Success"
