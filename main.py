import sys
import module_cmd
import psycopg2
from psycopg2.extras import RealDictCursor
import configparser
import pika

# Read Config File
config = configparser.ConfigParser()
config.read('config.ini')
print(config.get('APP', 'ENVIRONMENT'))
# Connect Postgres
pg_db = psycopg2.connect(user=config.get('DATABASE', 'USER'),
                         password=config.get('DATABASE', 'PASSWORD'),
                         host=config.get('DATABASE', 'HOST'),
                         port=config.get('DATABASE', 'PORT'),
                         database="FoodDB",
                         cursor_factory=RealDictCursor)

print("Connect Postgres Success")
# Connect RabbitMQ

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# Run App


if len(sys.argv) < 2:
    print("Missing Args")
else:
    if len(sys.argv) == 2:
        if sys.argv[1] == 'api':
            module_cmd.run_api(pg_db, channel)
        elif sys.argv[1] == 'consumer':
            module_cmd.run_consumer(channel)
    else:
        print("Hello World")
