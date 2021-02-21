from abstract import AbstractConsumerModel
import json
import model
from concurrent.futures import ThreadPoolExecutor
import time


class SyncESFoodByList(AbstractConsumerModel):
    def __init__(self, queue_name, food_rp, elasticsearch_manager):
        self.queue_name = queue_name
        self.food_rp = food_rp
        self.elasticsearch_manager = elasticsearch_manager

    def callback(self, ch, method, properties, body):
        try:
            print(self.queue_name)
            print(" [x] Received %r" % body.decode())

            list_data = json.loads(body.decode())

            def sync_es_food(food_document):
                print("Sync elasticsearch with food id: ", food_document["id"])
                self.elasticsearch_manager.index_document_food(food_document)

            with ThreadPoolExecutor(max_workers=3) as executor:
                data = {executor.submit(sync_es_food, item): item for item in list_data}

        except Exception as e:
            print(e)
        ch.basic_ack(delivery_tag=method.delivery_tag)
