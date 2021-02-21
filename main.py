import sys
import module_cmd
import provider

config = provider.get_config()

pg_db = provider.connection_pg_db(config)
mq_channel_connect = provider.connection_rabbitmq(config)
redis_connect = provider.get_redis(config)
# es = provider.get_es()
# Run App


if len(sys.argv) < 2:
    print("Missing Args")
else:
    if len(sys.argv) == 2:
        if sys.argv[1] == 'api':
            module_cmd.run_api(pg_db, mq_channel_connect, redis_connect)
        elif sys.argv[1] == 'consumer':
            module_cmd.run_consumer(mq_channel_connect, pg_db)
    else:
        print("Hello World")
