from huey import RedisHuey
huey_queue = RedisHuey('my-queue', host="localhost", port=6379)

def run_consumer():
    while True:
        try:
            huey_queue.dequeue()
        except Exception as e:
            print("Error processing task:", e)

if __name__ == "__main__":
    run_consumer()