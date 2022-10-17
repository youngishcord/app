from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()

manager = Task(tasks['manager'])
inspector = Task(tasks['inspector'])

s_manager = manager.s().set(queue='managers')
s_inspector = inspector.s().set(queue='inspectors')

ch = s_inspector | s_manager

data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip'
}

data1 = {
    'tasks':'qwerty',
    'body':'qwerty',
    'filename':'zxcvb.jpg',
    'valid':True
}

data2 = {
    'tasks':'qwerty',
    'body':'qwerty',
    'filename':'zxcvb.jpg',
    'valid':False
}

valid_data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip',
    'valid':True,
    'path':'/path',
}

valid_data1 = {
    'tasks':'qwerty',
    'body':'qwerty',
    'filename':'zxcvb.jpg',
    'valid':True,
    'path':'/path',
}

#print(ch.delay(data).get())

class TestManager(unittest.TestCase):

    def test_base(self):
        self.assertEqual(ch.delay().get(), None)

    def test_no_dict(self):
        self.assertEqual(ch.delay().get(), None)
        self.assertEqual(ch.delay([]).get(), None)
        self.assertEqual(ch.delay('asdf').get(), None)
        self.assertEqual(ch.delay(123).get(), None)

    def test_empt(self):
        self.assertEqual(ch.delay({}).get(), None)
        self.assertEqual(ch.delay({'tasks':'TestsFooBar','body':'',}).get(), None)
        
    def test_ext(self):
        self.assertEqual(ch.delay(data1).get(), None)
        self.assertEqual(ch.delay(data2).get(), None)

    def test_valid(self):
        self.assertEqual(ch.delay({'tasks':'TestsFooBar','body':'','filename':'arc.zip',}).get(), valid_data)
        self.assertEqual(ch.delay({'tasks':'TestsFooBar','body':'','filename':'arc.zip','valid':False}).get(), valid_data)


if __name__ == '__main__':
    unittest.main()
    pass
