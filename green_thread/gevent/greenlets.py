import gevent

"""
greenlet은 일종의 pesudo-threads이다.  
green thread 혹은 micro thread라고 알려져 있으며 os단의 thread가 아니라 애플리케이션 단의 thread이다.  

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

# 알아서 스케쥴링 됨
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(wow),
])