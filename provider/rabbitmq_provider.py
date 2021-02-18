import pika


def connection_rabbitmq():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print("Connect RabbitMQ")
    return channel
