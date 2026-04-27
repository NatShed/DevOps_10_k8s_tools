import os
import time
import redis
import socket
from flask import Flask

app = Flask(__name__)

DB_HOST = os.getenv('REDIS_HOST', 'redis')
MY_ENV = os.getenv('ENV', 'unknown')

cache = redis.Redis(host=DB_HOST, port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    hostname = socket.gethostname()
    return f'Hello World! I have been seen {count} times. My name is: {hostname} My env: {MY_ENV}\n'
