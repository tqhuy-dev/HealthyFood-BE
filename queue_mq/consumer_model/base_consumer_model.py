from abstract import AbstractConsumerModel
from .add_material_consumer_model import AddMaterialConsumerModel
from .update_material_consumer import UpdateMaterialConsumer
from repository import MaterialRepository, FoodRepository
from enum_class import QueueNameEnum
from .sync_es_food_by_list_consumer_model import SyncESFoodByList


class DefaultConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print("Default")
        print(" [x] Received %r" % body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)


def switch_consumer(queue_name, pg_db):
    if queue_name == QueueNameEnum.AddMaterial.value:
        material_rp = MaterialRepository(pg_db)
        return AddMaterialConsumerModel(queue_name, material_rp)
    elif queue_name == QueueNameEnum.UpdateMaterial.value:
        material_rp = MaterialRepository(pg_db)
        return UpdateMaterialConsumer(queue_name, material_rp)
    elif queue_name == QueueNameEnum.SyncESFoodByList.value:
        food_rp = FoodRepository(pg_db)
        return SyncESFoodByList(queue_name, food_rp)
    return DefaultConsumerModel("")
