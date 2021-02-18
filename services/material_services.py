import model
import abc
from enum_class import StatusMaterialTypeEnum
import pandas as pd


class AbstractMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_material_sv(self, request):
        pass

    @abc.abstractmethod
    def get_material_sv(self, request):
        pass

    @abc.abstractmethod
    def update_file_list_material(self, request):
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

    def update_file_list_material(self, request):
        try:
            if "file" not in request.files:
                return False, "File must not empty"
            file = request.files["file"]
            path_file = file.filename.split(".")
            if len(path_file) > 1 and path_file[len(path_file) - 1] != "csv":
                return False, "File CSV"
            df = pd.read_csv(file)
            list_material = []
            count = 0
            for index in range(len(df)):
                if count < 5:
                    material = model.MaterialModel(0,
                                                   df["Name"][index],
                                                   df["Status"][index],
                                                   df["Quantity"][index],
                                                   df["Unit"][index],
                                                   df["Description"][index],
                                                   df["MaterialType"][index],
                                                   df["Image"][index],
                                                   df["Price"][index])
                    list_material.append(material)
                    count += 1
                    # self.material_rp.add_material_by_list(list_material)
                else:
                    list_material = []
                    count = 0
        except:
            return False, "Internal Error"
        return True, "Success"
        pass
