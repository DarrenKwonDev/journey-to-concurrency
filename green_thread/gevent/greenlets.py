import gevent

"""
http://www.gevent.org/intro.html
"""

def foo():
    print('Running in foo')
    gevent.sleep(1) 
    print('foo done')

def bar():
    print('context switching to bar')
    gevent.sleep(5)
    print('bar done')

def wow():
    print("context switching to wow")
    gevent.sleep(3)  
    print("wow done")

# http://www.gevent.org/api/gevent.html#gevent.joinall
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(wow),
])