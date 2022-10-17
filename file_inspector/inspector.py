from celery import Celery
import os


broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'inspector',
    backend='rpc://',
    broker=broker_addr,
)

def get_ext(name):
    ext = name.split('.')[1]
    return ext

@app.task
def inspector(data=None):
    print('inspector called')
    print('recv ', data)
    if isinstance(data, dict):
        try:
            if data['filename']:
                if get_ext(data['filename']) == 'zip':
                    data['valid'] = True
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
    print(inspector(data))
