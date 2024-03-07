from huey import RedisHuey
from huey.exceptions import HueyException
import redis

redis_client = redis.Redis(host="35.197.123.183", port=6379, db=0)
huey_queue = RedisHuey('my-queue', host="35.197.123.183", port=6379)

@huey_queue.task()
def create_item(key: str, value: str):
    redis_client.set(key,value)

@huey_queue.task()
def update_item(key: str, value: str):
    redis_client.set(key,value);    

@huey_queue.task()
def read_item(key: str):
    return redis_client.get(key);    

@huey_queue.task()
def delete_item(key: str):
    redis_client.delete(key) 