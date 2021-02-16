import model
import abc


class AbstractMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_material(self, request):
        pass


class MaterialServices(AbstractMaterialServices):
    def __init__(self, material_rp):
        self.material_rp = material_rp

    def add_material(self, request):
        data = request.json
        material = model.MaterialModel(0,
                                       data["name"],
                                       data["status"],
                                       data["quantity"],
                                       data["unit"],
                                       data["description"],
                                       data["material_type"],
                                       ",".join(data["image"]))

        try:
            self.material_rp.add_material(material)
        except:
            return False, "Internal Error:Execute Error"
        return True, "Success"
