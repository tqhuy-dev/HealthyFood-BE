from abstract import AbstractConsumerModel


class AddMaterialConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


class TestConsumerModel(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)
