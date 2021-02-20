import model
import abc
from enum_class import StatusMaterialTypeEnum, QueueNameEnum
import pandas as pd
from common import material_common_logic


class AbstractMaterialServices(abc.ABC):
    @abc.abstractmethod
    def add_material_sv(self, request):
        pass

    @abc.abstractmethod
    def get_material_sv(self, request):
        pass

    @abc.abstractmethod
    def set_material_type_rp(self, material_type_rp):
        pass

    @abc.abstractmethod
    def set_mq_channel_manager(self, mq_channel_manager):
        pass


class MaterialServices(AbstractMaterialServices):
    def __init__(self, material_rp):
        self.material_rp = material_rp
        self.material_type_rp = None
        self.mq_channel_manager = None

    def set_material_type_rp(self, material_type_rp):
        self.material_type_rp = material_type_rp

    def set_mq_channel_manager(self, mq_channel_manager):
        self.mq_channel_manager = mq_channel_manager

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
        except Exception as e:
            print(e)
            return False, "Internal Error:Execute Error"
        return True, "Success"

    def get_material_sv(self, request):
        try:

            body_filter = material_common_logic.build_filter_condition_request(request)
            data_material = self.material_rp.get_material(body_filter)
            result = []
            for item in data_material:
                result.append(item.get_dict())

            return True, result
        except Exception as e:
            print(e)
            return False, "Internal Error"
