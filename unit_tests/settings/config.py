tasks = {
    'add': 'tasks.add',
    'foo': "tasks.foo",
    'bar': "tasks.bar",
    'inspector':'inspector.inspector',
    'manager':'manager.manager',
}

queues = {
    
}

ROUTES = {
    "tasks.one":{"queue":"ones"}, 
    "tasks.add":{"queue":"ones"},
    "tasks.two":{"queue":"twos"},
    "tasks.three":{"queue":"threes"},
    "tasks.foo":{"queue":"foo"},
    "tasks.bar":{"queue":"bar"},
    'inspector.inspector':{'queue':'inspectors'},
    'manager.manager':{'queue':'managers'},
}