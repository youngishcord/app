from celery import Celery
import os
import socket
import hashlib



broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'filestore',
    backend='rpc://',
    broker=broker_addr,
)

def get_ext(name):
    ext = name.split('.')[1]
    return ext

def md5(path: str, filename: str) -> str:
    hash_md5 = hashlib.md5()
    with open(path + filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

@app.task
def filestore(data=None):
    print('filestore called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    filename = data['filename']
    ip = data['ip']
    port = data['port']
    hash = data['hash']
    
    connection = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    connection.connect((ip, port))

    arr = []
    while True:
        arr.append(connection.recv(1024))
        if arr[-1] == b'':
            break
    full = b''.join(arr)

    try:
        os.makedirs('./data')
    except Exception as ex:
        print(ex)

    with open('./data/' + filename, 'wb') as file:
        file.write(full)
        file.close()

    md = md5('./data/', filename)

    print(hash)
    print(md)

    data['path'] = './data/'

    return data


if __name__ == '__main__':
    data = {'task': 'upload',
    'ip': '192.168.1.35',
    'port': 9991,
    'filename': 'img.zip',
    'hash': 'e5b64259a734824dd0ef58c6a82f7e97'}
    filestore(data)