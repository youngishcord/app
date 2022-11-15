from settings.create import create_celery
from settings.config import tasks
import unittest

Task = create_celery()

mongo_metadata = Task(tasks['collection_manager'])
print(mongo_metadata)

print(mongo_metadata.delay('ping').get())

mongo_metadata = mongo_metadata.s().set(queue='collection_manager')

#mongo_metadata.delay('ping').get()

data = {
    'tasks':'qwerty',
    'body':'qwerty',
    'filename':'01_Баукова.zip',
    'valid':True,
    'path':'./data/01_Баукова/',
    'metadata':'01_Баукова.json',
}

print(mongo_metadata.delay('ping').get())

#class TestExt(unittest.TestCase):
#
#    def test_no_dict(self):
#        self.assertEqual(inspector.delay().get(), None)
#        self.assertEqual(inspector.delay([]).get(), None)
#        self.assertEqual(inspector.delay('asdf').get(), None)
#        self.assertEqual(inspector.delay(123).get(), None)
##
#    def test_empt(self):
#        self.assertEqual(inspector.delay({}).get(), None)
#        self.assertEqual(inspector.delay({'tasks':'TestsFooBar','body':'',}).get(), None)
##
#    def test_no_zip(self):
#        self.assertEqual(inspector.delay(data1).get(), None)
##
#    def test_zip(self):
#        self.assertEqual(inspector.delay(data).get(), valid_data)
#        self.assertEqual(inspector.delay(data2).get(), valid_data)


if __name__ == '__main__':
    unittest.main()
    pass
