class A(object):
    a = 10
    def bow(self):
        print 'bow'
        
    def __getattr__(self, name):
        print 'getattr', name
        
    def __getattribute__(self, name):
        print 'attribute', name

class B(object):
    def __getattr__(self, name):
        print name

class Bar(object):
    def __init__(self):
        pass
    
class Baz:
    pass

class Foo(Bar, Baz, A, B, object):
    def __getattr__(self, name):
        print 'getattr Foo'
        
    def __init__(self):
        Bar.__init__(self)

f = Foo()
print Foo.__mro__
f.x

print super(Foo, f).a
print super(Foo, f).bow()
print super(Foo, f).x

print type(Baz)
