import random


class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        print self # current class Die object will call
        print instance # by which class object called this die attribute
        print owner #Name of the class being called by instance
        return int(random.random() * self.sides) + 1


class A(object):
    d1 = Die()
    d2 = Die(10)
    d3 = Die(12)


class B(object):
    e1 = Die()


a1 = A()
b1 = B()
c1 = C()
print a1.d1
print b1.e1
print c1.e1

"""
print a1.d1
<__main__.Die object at 0xb7736fcc>
<__main__.A object at 0xb74b910c>
<class '__main__.A'>
6
-----------------------
print b1.e1
<__main__.Die object at 0xb74b908c>
<__main__.B object at 0xb74b912c>
<class '__main__.B'>
2

"""