from abstract import AbstractConsumerModel
from .add_material_consumer_model import AddMaterialConsumerModel, TestConsumerModel


class DefaultConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print("Default")
        print(" [x] Received %r" % body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)


def switch_consumer(queue_name):
    if queue_name == "AddMaterial":
        return AddMaterialConsumerModel(queue_name)
    elif queue_name == "Test":
        return TestConsumerModel(queue_name)
    return DefaultConsumerModel("")
