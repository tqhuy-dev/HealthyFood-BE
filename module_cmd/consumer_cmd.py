import json
from queue_mq import switch_consumer
import pandas as pd


def run_consumer(mq_channel_connect, pg_db, es):
    mq_channel_connect.basic_qos(prefetch_count=1)
    with open("queue_config.json") as data_json_file:
        data = json.load(data_json_file)
        for item in data["Message"]:
            consumer_model = switch_consumer(item["QueueName"], pg_db, es)
            mq_channel_connect.basic_consume(queue=consumer_model.queue_name,
                                             on_message_callback=consumer_model.callback)
    print("Running Consumer....")
    mq_channel_connect.start_consuming()


def test():
    tuples = []
    values = []
    for index in range(500):
        tuples.append(
            (index, index, index, index, index, index, index, index, index, index, index, index, index, index))
        tuples.append(
            (index, index, index, index, index, index, index, index, index, index, index, index, index, index))
        values.append([1, 2])
        values.append([1, 2])
    index = pd.MultiIndex.from_tuples(tuples)
    df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
    df.to_excel("resource/food.xlsx", merge_cells=True)
