class D(object):
    def __init__(self, a1, a2=None, a3=None):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __get__(self, instance, owner):
        return self.a1

    def __set__(self, instance, value=None):
        self.a1 = value


class A(object):
    d1 = D('Hi', 10, 5)
    x = 10



y1 = A()
print y1.x
print y1.d1

y1.d1 = 'Bye'
print y1.d1


"""
10
Hi
Bye
""
 data descriptors  always override instance dictionaries.  non-data descriptors may be overridden
by instance dictionaries
"""

"""
