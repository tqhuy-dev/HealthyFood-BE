from abstract import AbstractConsumerModel
import json
from model import MaterialModel


class AddMaterialConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name, material_repo):
        self.queue_name = queue_name
        self.material_repo = material_repo

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
        try:
            data_mt = json.loads(body.decode())
            list_material = []
            for item in data_mt:
                mt_item = MaterialModel(0,
                                        item["name"],
                                        item["status"],
                                        item["quantity"],
                                        item["unit"],
                                        item["description"],
                                        item["material_type"],
                                        item["image"],
                                        item["price"])
                list_material.append(mt_item)

            self.material_repo.add_material_by_list(list_material)
        except Exception as e:
            print("Queue Error")
            print(e)
        ch.basic_ack(delivery_tag=method.delivery_tag)


class TestConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)
