from celery import Celery
import os
from celery.exceptions import *
import celery


broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'exceptions1',
    backend='rpc://',
    broker=broker_addr,
)

def get_ext(name):
    ext = name.split('.')[1]
    return ext

@app.task
def exceptions1(data=None):
    print('exc1 called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    if data['body'].count('foo') >= 2:
        print('TOO MUCH FOO')
        raise celery.exceptions.CeleryError
    data['body'] += '-foo-'
    return data

if __name__ == '__main__':
    data = {
    'tasks':'TestsFooBar',
    'body':'-foo--foo-',
    'filename':'arc.zip'
    }
    print(exceptions1(data))
