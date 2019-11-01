class A(object):
    def __init__(self):
        print 'init A'
        
    def foo(self):
        print 'A.foo'

class B(object):
    def __init__(self):
        print 'init B'
    
    def foo(self):
        print 'B.foo'


class DC(A, B):
#omitting this init causes A.__init__ to be invoked
    def __init__(self):
        print 'init DC'        
        
    def foo(self):
        print 'DC.foo'

#causes __init__ to be autoinvoked ONCE and this will propagate 
#up the class hierarchy
f = DC()
f.foo()

#skips DC.foo and searches the base classes
super(DC, f).foo()
