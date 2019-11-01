class Bar(object):
    pass

class Foo(object):
    def __foo__(self):
        print 'hi'

f = Foo()
f.__foo__()


x = f.__foo__
x()

#g = Foo()
#b = Bar()
x = Foo.__foo__
x(g)
x(b)

