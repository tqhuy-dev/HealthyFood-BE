import redis


def get_redis(config):
    r = redis.Redis(host=config.get('REDIS', 'HOST'), port=config.get('REDIS', 'PORT'), db=0)
    print("Connect Redis")
    return r
