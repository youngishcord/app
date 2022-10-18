import time
from celery import Celery
import os


broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'manager',
    backend='rpc://',
    broker=broker_addr,
)


@app.task
def manager(data=None):
    print('manager called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    if isinstance(data, dict) and len(data) != 0:
        try:
            if data['valid'] == True:
                print('downloading')
                for i in range(5):
                    print(f'{(i+1)*20}%')
                    time.sleep(0.5)
                data['path'] = '/path'
                return data
        except:
            return None
    return None


if __name__ == '__main__':
    data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip'
    }
    print(manager(data))
