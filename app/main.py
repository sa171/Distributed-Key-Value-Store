from fastapi import FastAPI
from pydantic import BaseModel
from huey import RedisHuey
from huey.exceptions import HueyException
import redis

app = FastAPI()
#redis-service
redis_client = redis.Redis(host="redis-service", port=6379, db=0)
huey_queue = RedisHuey('my-queue', host="localhost", port=6379)

class Item(BaseModel):
    key: str
    value: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/item")
async def insert(item:Item):
    #todo
    create_item(item.key, item.value)
    return {"message": "Success"}

@app.put("/item")
async def update(item:Item):
    #todo
    update_item(item.key, item.value)
    return {"message": "Success"}

@app.delete("/item/{key}")
async def delete(key:str):
    #todo
    delete_item(key)
    return {"message": "Success"}

@app.get("/item/{key}")
async def read(key:str):
    #todo
    try:
        value = read_item(key).get(blocking = True, timeout=5)
        if value is None:
            return "{} does not exist in the store".format(key)
        return value
    except HueyException:
        return "Task took too long to complete, try again!"

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

