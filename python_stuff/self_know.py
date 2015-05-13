class A(object):

    def __init__(self):
        self.i = 5

    @staticmethod
    def one():
        i = 10
        print i
        print "Hi"

    @classmethod
    def two(cls):
        i = 15
        print i
        print "2nd hi"

    def third():
        return "3rd hi"

    def test(self, x):
        o1 = {1: 10, 2: 30, 3: 35} #here we can avoid if statement using dictionary
        print o1[x]


class B(A):

    def __init__(a):
        super(B, a).__init__()
        a.j = 10

    @staticmethod
    def one():
        j = 30
        print j
        print "HI from subclass"

