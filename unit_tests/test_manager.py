from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()

inspector = Task(tasks['manager'])

s_inspector = inspector.s().set(queue='managers')

data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip',
    'valid':True
}

data1 = {
    'tasks':'qwerty',
    'body':'qwerty',
    'filename':'zxcvb.jpg',
    'valid':True
}

data2 = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip',
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

class TestManager(unittest.TestCase):

    def test_no_dict(self):
        self.assertEqual(inspector.delay().get(), None)
        self.assertEqual(inspector.delay([]).get(), None)
        self.assertEqual(inspector.delay('asdf').get(), None)
        self.assertEqual(inspector.delay(123).get(), None)

    def test_empt(self):
        self.assertEqual(inspector.delay({}).get(), None)
        self.assertEqual(inspector.delay({'tasks':'TestsFooBar','body':'',}).get(), None)
        self.assertEqual(inspector.delay({'tasks':'TestsFooBar','body':'','filename':'arc.zip',}).get(), None)
        self.assertEqual(inspector.delay({'tasks':'TestsFooBar','body':'','filename':'arc.zip','valid':False}).get(), None)

    def test_valid(self):
        self.assertEqual(inspector.delay(data).get(), valid_data)
        self.assertEqual(inspector.delay(data1).get(), valid_data1)


if __name__ == '__main__':
    unittest.main()
    pass
