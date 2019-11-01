class c1(object):
    def miaow(self):
        pass

class c2(object):
    def bowbow(self):
        pass


class c3:
    def scritchscritch(self):
        pass


class Noise(c1, c2, c3):
    def __init__(self, x = None):
        if x == None:
            self.x = 10


n1 = Noise()
print dir(n1)
print
print n1.__dict__
print n1.__class__
print n1.__class__.__dict__
print n1.__class__.__bases__
for c in n1.__class__.__bases__:
    print c.__dict__
    print c.__bases__
