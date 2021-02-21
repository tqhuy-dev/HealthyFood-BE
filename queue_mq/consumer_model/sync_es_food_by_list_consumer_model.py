from abstract import AbstractConsumerModel


class SyncESFoodByList(AbstractConsumerModel):
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print(self.queue_name)
        print(" [x] Received %r" % body.decode())
