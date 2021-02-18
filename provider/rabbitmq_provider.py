import pika


def connection_rabbitmq(config):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.get('RABBITMQ', 'HOST')))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print("Connect RabbitMQ")
    return channel
