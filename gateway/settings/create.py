import os
from celery import Celery
from celery import Task as BaseTask
from .config import ROUTES


def create_celery():

    broker_addr = os.environ.get(
        'BROKER',
        'pyamqp://guest@localhost:5672//',
    )

    celery = Celery(
        'unit_test',
        backend='rpc://',
        broker=broker_addr
    )

    conf = celery.conf
    conf.task_routes = ROUTES
    celery.conf.update(conf)

    class Task(BaseTask):
        def __init__(self, name, *args, **kwargs):
            super(BaseTask, self).__init__(*args, **kwargs)
            self.name = name

    return Task