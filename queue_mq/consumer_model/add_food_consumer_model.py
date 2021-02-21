from abstract import AbstractConsumerModel


class AddFoodConsumerModel(AbstractConsumerModel):

    def __init__(self, queue_name, food_rp):
        self.food_rp = food_rp
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        try:
            print(self.queue_name)
            print(" [x] Received %r" % body.decode())
        except Exception as e:
            print(e)
