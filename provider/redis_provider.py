import redis
import common


# r = redis.Redis()
# r.smembers()


def get_redis(config):
    r = redis.Redis(host=config.get('REDIS', 'HOST'), port=config.get('REDIS', 'PORT'), db=0)
    print("Connect Redis")
    return r


class RedisManager(object):
    def __init__(self, redis_mn):
        self.redis_mn = redis_mn

    def init_set_redis(self, key, data):
        list_str = common.convert_dict_list_to_json_str(data)
        self.redis_mn.sadd(key, *list_str)

    def get_set_redis(self, key):
        try:
            data_redis = self.redis_mn.smembers(key)
            return data_redis
        except:
            return []
