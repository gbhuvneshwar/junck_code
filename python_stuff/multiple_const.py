class A(object):
    def __init__(self):
        print "HI from no args"

    def __init__(self, a1):
        print "hi from single args"

    def __init__(self, a2, a3):
        print "hi from double args"

    def Hi(self):
        print "HI"

    def Hi(self, name):
        self.name = name
        print self.name



#a1 = A()

#a2 = A(10)

a3 = A('shiva', 'sai')

print a3.Hi('krishna')

"""
bash-4.1$ python multiple_const.py
Traceback (most recent call last):
  File "multiple_const.py", line 14, in <module>
    a1 = A()
TypeError: __init__() takes exactly 3 arguments (1 given)


"""