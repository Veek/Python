class A(object):
    def foo(self):
        print 'A'

class B(A):
    def foo(self):
        print 'B'
        super(B, self).foo()

class C(A):
    def foo(self):
        print 'C'
        super(C, self).foo()

class D(B,C):
    def foo(self):
        print 'D'
        super(D, self).foo()

    def __getattribute__(self, name):
        try:
            print 'try', name
            x = super(D, self).__getattribute__(name)
            print x
        except AttributeError:
            print 'Attribute Error'
        else:
            print 'else'
            return x

d = D()

#d.foo is looked up, this implies D.__getattribute__ is called
#try/super runs and skips D when locating 'foo' so the default
#implementation within 'object is used. Therefore we are doing
#super(D, self).object's__getattribute__(self, name)
#super populates __getattribute__'self'  with 'self' the local
#instance - so we are looking for 'name' in the local instance
#therefore D/foo() runs with 'd' as the instance
d.foo() #-->D
#then D.foo( super() is invoked. This will skip D and bind to B
# so B.foo runs so you get 'D' 'B' 'C' 'A'

#to avoid the 'D'
#def __getattribute__(self, name):
#    return getattr(super(D, self), name)
#is basically return superObj.name(self) and 'name' has to be 
#located by skipping 'D'

