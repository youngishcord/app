from math import expm1
from settings.config import queues

from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()


data = {
    'tasks':'TestsFooBar',
    'body':'',
}

#exc1 = Task(tasks['exceptions1'])
#exc2 = Task(tasks['exceptions2'])

exc1 = queues['exceptions1']
exc2 = queues['exceptions2']

print(exc1)
print(exc2)

#exc1 = exc1.s().set(queue='exceptions1Q')
exc2 = exc2.s().set(queue='exceptions2Q')

#print(exc1.delay('ping').get())
#print(exc2.delay('ping').get())
#
# t_foo.delay(data).get()
#ch2 = exc1|exc2
#print(ch2(data).get())
ch = exc1|exc1|exc2|exc2|exc2|exc2
#print(ch.delay(data).get())
print(ch.delay('ping').get())


#print(ee1.delay(data).get())
#print(ee2.delay(data).get())
#
#ch = ee1|ee2|ee1|ee2
#
#print(ch.delay('ping').get())

#class TestSum(unittest.TestCase):
#
#    def test_sum(self):
#        self.assertEqual(ch.delay(data).get()['body'],'-foo--foo--foo--bar--bar--foo--bar-')


if __name__ == '__main__':
#    unittest.main()
    pass

