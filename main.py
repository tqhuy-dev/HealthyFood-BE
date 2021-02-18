import sys
import module_cmd
import provider

config = provider.get_config()

pg_db = provider.connection_pg_db(config)
mq_channel = provider.connection_rabbitmq(config)
redis_manager = provider.get_redis(config)
# Run App


if len(sys.argv) < 2:
    print("Missing Args")
else:
    if len(sys.argv) == 2:
        if sys.argv[1] == 'api':
            module_cmd.run_api(pg_db, mq_channel, redis_manager)
        elif sys.argv[1] == 'consumer':
            module_cmd.run_consumer(mq_channel)
    else:
        print("Hello World")
