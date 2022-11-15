from celery import Celery
import os
import json
import time

broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//'
)

app = Celery('bar', backend='redis://localhost:6379', broker=broker_addr)

@app.task
def bar(data):
    print('bar called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    data['body'] += '-bar-'
    time.sleep(1)
    return data

# https://dpaste.org/ka4v5