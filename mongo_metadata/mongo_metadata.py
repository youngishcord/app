from celery import Celery
import os
import pymongo
import json
import requests


broker_addr = os.environ.get(
    'BROKER',
    'pyamqp://guest@localhost:5672//',
)

app = Celery(
    'orthanc_upload',
    backend='rpc://',
    broker=broker_addr,
)

def get_ext(name):
    ext = name.split('.')[1]
    return ext


@app.task
def mongo_metadata(data=None):
    print('mongo_metadata called')
    print(f'recv {data}')

    if data == 'ping':
        for _ in range(5):
            print('THIS IS PING')
        return data
    
    if isinstance(data, dict):

        try:
            #print(data['metadata'])
            if data['metadata']:
                
                with open(data['path'] + data['metadata'], 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                print(metadata)

                client = pymongo.MongoClient('localhost', 27017)
                client.server_info()
                db = client['metadata']
                collection = db[metadata['second name']]
    
                collection.insert_one(metadata)
    
                return data

            else:
                id = data['ids']['patientid']
                metadata = requests.get(f'http://localhost:8042/patients/{id}?requestedTags=PatientName;PatientBirthDate;PatientID;PatientSex;SeriesDate;Manufacturer;ManufacturerModelName;StudyInstanceUID')
                metadata = json.loads(metadata.content.decode('utf-8'))
                print(metadata)
                client = pymongo.MongoClient('localhost', 27017)
                client.server_info()
                db = client['metadata']
                collection = db[metadata['RequestedTags']['PatientName']]
    
                collection.insert_one(metadata)
    
                return data
                
                # for id in data['ids']['seriesid']:
                #     inf = requests.get(f'http://localhost:8042/patients/{id}?requestedTags=PatientName;PatientBirthDate;PatientID;PatientSex;SeriesDate;Manufacturer;ManufacturerModelName;StudyInstanceUID')
                    

        except Exception as ex:
            print(ex)
            return None
    return None


if __name__ == '__main__':
    data = {
        'tasks':'qwerty',
        'body':'qwerty',
        'filename':'zxcvb.jpg',
        'valid':True,
        'path':'./data/01_Баукова/',
        'ids':{
            'patientid':'0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043',
            'seriesid':[
                '0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043',
            ],
        },
        'metadata':'',#'01_Баукова.json',
    }
    print(mongo_metadata(data))
