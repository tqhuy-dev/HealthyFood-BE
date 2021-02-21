from abstract import AbstractConsumerModel
import json
import model


class SyncESFoodByList(AbstractConsumerModel):
    def __init__(self, queue_name, food_rp):
        self.queue_name = queue_name
        self.food_rp = food_rp

    def callback(self, ch, method, properties, body):
        try:
            print(self.queue_name)
            print(" [x] Received %r" % body.decode())
            list_data = json.loads(body.decode())
            list_food = []
            for item in list_data:
                food = model.Food(0,
                                  item["name"],
                                  item["type_food"],
                                  item["price"],
                                  item["status"],
                                  item["order_total"],
                                  item["rate"],
                                  item["unit"])
                food.set_image(item["image"])
                list_food.append(food)

            # self.food_rp.add_list_food(list_food)
        except Exception as e:
            print(e)
