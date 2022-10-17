from itertools import chain
import queue
from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()

t_foo = Task(tasks['foo'])
t_bar = Task(tasks['bar'])


foo = t_foo.s().set(queue='foo')
bar = t_bar.s().set(queue='bar')

data = {
    'tasks':'TestsFooBar',
    'body':'',
}

# t_foo.delay(data).get()

ch = foo|foo|foo|bar|bar|foo|bar
# print(ch.delay(data).get())

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(ch.delay(data).get()['body'],'-foo--foo--foo--bar--bar--foo--bar-')


if __name__ == '__main__':
    unittest.main()

