from celery import Celery
import os
import json

broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//'
)

app = Celery('bar', backend='rpc://', broker=broker_addr)

@app.task
def bar(data):
    print('bar called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    data['body'] += '-bar-'
    return data