import redis


def get_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    print("Connect Redis")
    return r
