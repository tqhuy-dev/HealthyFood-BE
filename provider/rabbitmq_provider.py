import pika
import json


def connection_rabbitmq(config):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.get('RABBITMQ', 'HOST'),
                                  virtual_host=config.get('RABBITMQ', 'VIRTUAL_HOST'),
                                  port=config.get('RABBITMQ', 'PORT')))
    channel = connection.channel()

    with open('queue_config.json') as json_config_file:
        data = json.load(json_config_file)
        for item in data["Message"]:
            if item["Active"]:
                channel.queue_declare(queue=item["QueueName"], durable=True)

    print("Connect RabbitMQ")
    return channel


class MQChannelManager(object):
    def __init__(self, mq_channel):
        self.mq_channel = mq_channel

    def publish_message(self, key, body_dict):
        print(json.dumps(body_dict))
        self.mq_channel.basic_publish(
            exchange='',
            routing_key=key,
            body=json.dumps(body_dict),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print("Queue: ", key, " receive message", body_dict)
