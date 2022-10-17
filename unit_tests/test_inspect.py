from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()

inspector = Task(tasks['inspector'])

s_inspector = inspector.s().set(queue='inspectors')

data = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.zip'
}

data1 = {
    'tasks':'TestsFooBar',
    'body':'',
    'filename':'arc.jpg'
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
    'valid':True
}

class TestExt(unittest.TestCase):

    def test_no_dict(self):
        self.assertEqual(inspector.delay().get(), None)
        self.assertEqual(inspector.delay([]).get(), None)
        self.assertEqual(inspector.delay('asdf').get(), None)
        self.assertEqual(inspector.delay(123).get(), None)

    def test_empt(self):
        self.assertEqual(inspector.delay({}).get(), None)
        self.assertEqual(inspector.delay({'tasks':'TestsFooBar','body':'',}).get(), None)

    def test_no_zip(self):
        self.assertEqual(inspector.delay(data1).get(), None)

    def test_zip(self):
        self.assertEqual(inspector.delay(data).get(), valid_data)
        self.assertEqual(inspector.delay(data2).get(), valid_data)


if __name__ == '__main__':
    unittest.main()
    pass
