class A(object):
    def __init__(self):
        print 'A'
        super(A, self).__init__()
    
class B(object):
    def __init__(self):
        print 'B'
        super(B, self).__init__()

class Foo(A, B):
    pass

print Foo.__mro__
f = Foo() #-->A B
#Foo has no __init__ so the default call to __init__ propogates
#to A. In A we are doing super(A, self) so we are skipping
#class 'A' and calling another __init__ with 'f'/self as the
#instance to super and __init__.

#this __init__ can only be found above 'A' in object, so we are
#doing object.__init__(f)
#the default implementation cannot find __init__ in f/Foo so 
#it looks at the next base class/B based on Foo.__mro__
