import pandas as pd
import model
from enum_class import QueueNameEnum
from common import material_common_logic


class MaterialFileServices(object):
    def __init__(self, material_rp, mq_channel_manager):
        self.material_rp = material_rp
        self.mq_channel_manager = mq_channel_manager

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
                material = model.MaterialModel(0,
                                               df["Name"][index],
                                               int(df["Status"][index]),
                                               int(df["Quantity"][index]),
                                               df["Unit"][index],
                                               df["Description"][index],
                                               int(df["MaterialType"][index]),
                                               df["Image"][index],
                                               int(df["Price"][index]))
                list_material.append(material.get_dict())
                count += 1
                if count == 5:
                    self.mq_channel_manager.publish_message(QueueNameEnum.AddMaterial.value, list_material)
                    list_material.clear()

            if len(list_material) > 0:
                self.mq_channel_manager.publish_message(QueueNameEnum.AddMaterial.value, list_material)
        except Exception as e:
            print(e)
            return False, "Internal Error"
        return True, "Success"
        pass

    def download_file_csv_material(self, request):
        try:
            body_filter = material_common_logic.build_filter_condition_request(request)
            data_material = self.material_rp.get_material(body_filter)

            matrix_material = {
                "Name": [],
                "Status": [],
                "Quantity": [],
                "Unit": [],
                "Description": [],
                "MaterialType": [],
                "Image": [],
                "Price": []
            }
            for material in data_material:
                item = material.get_dict()
                matrix_material["Name"].append(item["name"])
                matrix_material["Status"].append(item["status"])
                matrix_material["Quantity"].append(item["quantity"])
                matrix_material["Unit"].append(item["unit"])
                matrix_material["Description"].append(item["description"])
                matrix_material["MaterialType"].append(item["material_type"])
                matrix_material["Image"].append(item["image"])
                matrix_material["Price"].append(item["price"])

            df = pd.DataFrame({
                "Name": matrix_material["Name"],
                "Status": matrix_material["Status"],
                "Quantity": matrix_material["Quantity"],
                "Unit": matrix_material["Unit"],
                "Description": matrix_material["Description"],
                "MaterialType": matrix_material["MaterialType"],
                "Image": matrix_material["Image"],
                "Price": matrix_material["Price"],
            })
            df.to_csv("resource/material.csv", index=False)
            return True, "Success"
        except Exception as e:
            print(e)
            return False, "Internal Error"