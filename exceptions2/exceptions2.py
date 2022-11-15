from celery import Celery
import os

class TooMuchBar(Exception):
    '''очень много bar в тексте'''
    pass

broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'exceptions2',
    backend='rpc://',
    broker=broker_addr,
)

def get_ext(name):
    ext = name.split('.')[1]
    return ext

@app.task(autoretry_for=(TooMuchBar,), retry_kwargs={'max_retries': 5, 'countdown': 2})
def exceptions2(data=None,):
    print('exc1 called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    if data['body'].count('bar') >= 2:
        print('TOO MUCH BAR')
        raise TooMuchBar
        return data
    data['body'] += '-bar-'
    return data

if __name__ == '__main__':
    data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip'
    }
    print(exceptions2(data))
