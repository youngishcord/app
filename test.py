a = {'data':1234,'filename':'arch.zip'}
b = {'data':1234,'filename':''}

def qwer(data):
    if not data['filename']:
        print(data['filename'])

qwer(b)

print(len({}))