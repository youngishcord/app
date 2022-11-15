a = {'data':1234,'filename':'arch.zip'}
b = {'data':1234,'filename':''}

def qwer(data):
    if not data['filename']:
        print(data['filename'])

qwer(b)

print(len({}))


st = '-foo--foo--foo--bar--bar--foo--bar-'

print(st.count('foo'))

arr = [['c9521613-1dbd3727-e64dbb14-15fb2056-d31c7b2f', '455128bd-b59da3c7-46654c95-1dd2da2f-c06787a1']]

if 'c9521613-1dbd3727-e64dbb14-15fb2056-d31c7b2f' in arr:
    print('c9521613-1dbd3727-e64dbb14-15fb2056-d31c7b2f')