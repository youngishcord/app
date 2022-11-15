from .create import create_celery
from .q import ROUTES

Task = create_celery()

tasks = {
    'add': 'tasks.add',
    'foo': "tasks.foo",
    'bar': "tasks.bar",
    'inspector':'inspector.inspector',
    'manager':'manager.manager',
    'orthanc_upload':'orthanc_upload.orthanc_upload',
    'filestore':'filestore.filestore',
    'mongo_metadata':'mongo_metadata.mongo_metadata',
    'exceptions1':'exceptions1.exceptions1',
    'exceptions2':'exceptions2.exceptions2',
    'collection_manager': 'collection_manager.collection_manager'
}

#print(ROUTES['exceptions1.exceptions1']['queue'])
#print(ROUTES['exceptions1.exceptions1']['queue'])

queues = {
    'exceptions1':Task(tasks['exceptions1']).s().set(queues='exceptions1Q'),
    'exceptions2':Task(tasks['exceptions2']).s().set(queues='exceptions2Q'),
}