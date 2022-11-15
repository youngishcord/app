from celery import Celery
import os
import json
import time

broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery('foo', backend='redis://localhost:6379', broker=broker_addr)

@app.task
def foo(data):
    print('foo called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    data['body'] += '-foo-'
    time.sleep(1)
    return data


# https://dpaste.org/ggaNq