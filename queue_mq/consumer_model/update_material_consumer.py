from .base_consumer_model import AbstractConsumerModel
import json
from model import MaterialModel


class UpdateMaterialConsumer(AbstractConsumerModel):
    def __init__(self, queue_name, material_rp):
        self.queue_name = queue_name
        self.material_rp = material_rp

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
        try:
            data_mt = json.loads(body.decode())
            list_material = []
            for item in data_mt:
                mt_item = MaterialModel(item["id"],
                                        item["name"],
                                        item["status"],
                                        item["quantity"],
                                        item["unit"],
                                        item["description"],
                                        item["material_type"],
                                        item["image"],
                                        item["price"])
                list_material.append(mt_item)

            self.material_rp.update_material_by_list(list_material)
        except Exception as e:
            print(e)

        ch.basic_ack(delivery_tag=method.delivery_tag)
