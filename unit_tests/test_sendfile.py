import socket
from settings.create import create_celery
from settings.config import tasks
import sys
import hashlib

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

THIS_IP = get_ip()
SERVER_IP = "192.168.1.37"
LOCAL_IP = "127.0.0.1"
PORT_TO_SERVER = 9990
THIS_PORT = 9991
BUFFSIZE = 1024


try:
    filename = sys.argv[1]
except:
    filename = 'img.zip'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open('./storage/' + fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


Task = create_celery()

filestore = Task(tasks['filestore'])

s_filestore = filestore.s().set(queue='filestore')

#filestore.delay('ping').get()

task = {
    'task':'upload',
    'ip':THIS_IP,
    'port':THIS_PORT,
    'filename':filename,
    'hash':md5(filename),
}

filestore.delay(task)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((THIS_IP, THIS_PORT))
server.listen(0)

print('[x] waiting for connection ')
connection, address = server.accept()
print('[x] got a connection from ' + str(address))

with open('./storage/' + filename, 'rb') as file:
    connection.sendfile(file)
    file.close()
connection.close()
