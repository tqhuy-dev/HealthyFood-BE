import sys
import module_cmd
import psycopg2
from psycopg2.extras import RealDictCursor
import configparser
import pika
import provider

config = provider.get_config()

pg_db = provider.connection_pg_db(config)
channel = provider.connection_rabbitmq(config)
redis = provider.get_redis(config)
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
