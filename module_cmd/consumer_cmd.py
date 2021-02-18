import time


def run_consumer(mq_channel):
    print("Running Consumer....")

    mq_channel.basic_qos(prefetch_count=1)
    mq_channel.basic_consume(queue='task_queue', on_message_callback=callback)

    mq_channel.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
