import json
from queue_mq import switch_consumer


def run_consumer(mq_channel_connect, pg_db):
    mq_channel_connect.basic_qos(prefetch_count=1)
    with open("queue_config.json") as data_json_file:
        data = json.load(data_json_file)
        for item in data["Message"]:
            consumer_model = switch_consumer(item["QueueName"], pg_db)
            mq_channel_connect.basic_consume(queue=consumer_model.queue_name,
                                             on_message_callback=consumer_model.callback)
    print("Running Consumer....")
    mq_channel_connect.start_consuming()
