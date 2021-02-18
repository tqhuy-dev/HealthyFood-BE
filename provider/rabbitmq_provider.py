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
