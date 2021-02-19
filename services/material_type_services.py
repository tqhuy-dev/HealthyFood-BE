import model
import abc
from enum_class import StatusMaterialTypeEnum
import json
import sys


class AbstractMaterialTypeServices(abc.ABC):
    @abc.abstractmethod
    def add_material_type_sv(self, request):
        pass

    @abc.abstractmethod
    def get_material_type_sv(self, request):
        pass

    @abc.abstractmethod
    def set_redis_manager(self, redis_manager):
        pass


class MaterialTypeServices(AbstractMaterialTypeServices):
    def __init__(self, material_type_rp):
        self.material_type_rp = material_type_rp
        self.redis_manager = None

    def set_redis_manager(self, redis_manager):
        self.redis_manager = redis_manager

    def add_material_type_sv(self, request):
        data = request.json
        material_type = model.MaterialTypeModel(0, data["name"], data["status"])
        try:
            self.material_type_rp.add_material_type(material_type)
        except Exception as e:
            print(e)
            return False, "Internal Error: Execute Error"
        self.redis_manager.remove_key('material_type')
        return True, "Success"

    def get_material_type_sv(self, request):
        name_filter = request.args.get("name")
        status_filter = request.args.get("status")
        body_filter = {}
        is_filter = False
        if name_filter is not None and len(name_filter) > 0:
            body_filter["name"] = name_filter
            is_filter = True
        if status_filter is not None and status_filter > 0:
            body_filter["status"] = status_filter
            is_filter = True
        try:
            result = []
            if is_filter is False:
                data_mt_redis = self.redis_manager.get_set_redis('material_type')
                if len(data_mt_redis) > 0:
                    print("Get data from redis")
                    for item in data_mt_redis:
                        result.append(json.loads(item))
                    return True, result

            data_material_type = self.material_type_rp.get_material_type(body_filter)
            for item in data_material_type:
                item.status = StatusMaterialTypeEnum(item.status).name
                result.append(item.get_dict())

            if is_filter is False:
                self.redis_manager.init_set_redis('material_type', result)
            return True, result
        except Exception as e:
            print(e)
            print(sys.exc_info()[0])
            return False, "Internal Error: Execute Error"
