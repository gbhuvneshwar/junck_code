class A(object):
    def __init__(self, b=None):
        self.b = b
        print "Hi"

    def __repr__(self):
        return '%s%s' % (self.__class__, self.b)


class B(object):
    def __init__(self, a=None):
        self.a = a
        print "Hi from B"

    def __repr__(self):
        return '%s%s' % (self.__class__, self.a)


a1 = A()
b1 = B(a1)
a1.b1 = b1

print repr(b1)
