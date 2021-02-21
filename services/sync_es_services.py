from enum_class import QueueNameEnum


class SyncESFoodServices(object):
    def __init__(self, food_rp, mq_channel_manager):
        self.food_rp = food_rp
        self.mq_channel_manager = mq_channel_manager

    def sync_by_list_id(self, request):
        data = request.json
        filter_body = {
            "from_id": data["from_id"],
            "to_id": data["to_id"],
            "total": data["to_id"] - data["from_id"]
        }
        data_food = self.food_rp.get_all_food(filter_body)
        list_sync_food = []
        count = 0
        for food in data_food:
            food.price = int(food.price)
            list_sync_food.append(food.get_dict())
            count += 1
            if count == 12:
                self.mq_channel_manager.publish_message(QueueNameEnum.SyncESFoodByList.value, list_sync_food)
                list_sync_food.clear()
                count = 0

        if len(list_sync_food) > 0:
            self.mq_channel_manager.publish_message(QueueNameEnum.SyncESFoodByList.value, list_sync_food)
