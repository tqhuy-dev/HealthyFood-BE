import pandas as pd
import model
from enum_class import QueueNameEnum
from common import food_common_logic


class FoodFileServices(object):
    def __init__(self, food_rp, mq_channel_manager):
        self.food_rp = food_rp
        self.mq_channel_manager = mq_channel_manager

    def add_food_by_file(self, request):
        try:
            if "file" not in request.files:
                return False, "Bad Request"

            file = request.files
            df = pd.read_csv(file)

            list_food = []
            count = 0
            for index in range(len(df)):
                food = model.Food(0,
                                  df["Name"][index],
                                  df["TypeFood"][index],
                                  df["Price"][index],
                                  df["Status"][index],
                                  0,
                                  0,
                                  df["Unit"][index])
                food.set_image(df["Image"][index])
                list_food.append(food.get_dict())
                count += 1

                if count == 10:
                    self.mq_channel_manager.publish_message(QueueNameEnum.SyncESFoodByList.value, list_food)
                    list_food.clear()
                    count = 0

            if len(list_food) > 0:
                self.mq_channel_manager.publish_message(QueueNameEnum.SyncESFoodByList.value, list_food)

            return True, "Success"
        except Exception as e:
            print(e)
            return False, "Internal Error"

    def download_file_food(self, request):
        filter_body = food_common_logic.build_food_filter_condition_request(request)
        list_food = self.food_rp.get_all_food(filter_body)

        data_frame_arr = {
            "Id": [],
            "Name": [],
            "Price": [],
            "Status": [],
            "OrderTotal": [],
            "Rate": [],
            "TypeFood": [],
            "Unit": [],
            "Image": [],
            "Edited": []
        }

        for item in list_food:
            data_frame_arr["Id"].append(item.id)
            data_frame_arr["Name"].append(item.name)
            data_frame_arr["Price"].append(item.price)
            data_frame_arr["Status"].append(item.status)
            data_frame_arr["OrderTotal"].append(item.order_total)
            data_frame_arr["Rate"].append(item.rate)
            data_frame_arr["TypeFood"].append(item.type_food)
            data_frame_arr["Unit"].append(item.unit)
            if item.image is None:
                item.image = ""
            data_frame_arr["Image"].append(item.image)
            data_frame_arr["Edited"].append(0)

        df = pd.DataFrame(data_frame_arr)
        df.to_csv("resource/food.csv", index=False)
