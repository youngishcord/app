from celery import Celery
import os
import json

broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery('foo', backend='rpc://', broker=broker_addr)

@app.task
def foo(data):
    print('foo called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    data['body'] += '-foo-'
    return data