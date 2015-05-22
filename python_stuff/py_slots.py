class Myclass(object):
    def __init__(self, *args, **kwargs):
        self.x = 1
        self.y = 2

instance_1 = Myclass()
instance_2 = Myclass()
#print instance_1.__dict__
#print Myclass.__dict__

#op--> {'y': 2, 'x': 1}


class Myclass_1(object):
    __slots__ = ('x', 'y')

    def __init__(self, *args, **kwargs):
        self.x = 1
        self.y = 2

#instance_1 = Myclass_1()
#print instance_1.__dict__
#print instance_1.__slots__ # op --> ('x', 'y')

#print instance_1.x         # 1
#instance_1.x =100
#print instance_1.x          # 100

#instance_1.new_attr = 10    # whenever you define the slots class attribute  your dict class attribute will be gone
                            # we used slots to save some memory
                            #we can not add new attribute to the instance at run time if there is no dict
# print instance_1.new_attr
#print instance_1.__slots__


##read only attribute##

class Myclass_2(object):
    __slots__ = ('x', 'y')
    x = 5

    def __init__(self, *args, **kwargs):
        self.y = 10

"""
instance_1 = Myclass_2()
print instance_1.__slots__
print instance_1.x
print instance_1.y
instance_1.x = 25
print instance_1.x

('x', 'y')
5
10
Traceback (most recent call last):
  File "py_slots.py", line 48, in <module>
    instance_1.x = 25
AttributeError: 'Myclass_2' object attribute 'x' is read-only

"""


class Myclass3(object):
    __slots__ = ('x', 'y', '__dict__')
    x = 10

    def __init__(self, *args , **kwargs):
        self.y = 20

"""
instance_1 = Myclass3()
print instance_1.__slots__
print instance_1.x
instance_1.x = 100

print instance_1.x

print instance_1.__slots__

print instance_1.__dict__

instance_2 = Myclass3()
print instance_2.x

instance_1.new_attr = 50

print instance_1.new_attr
print instance_1.__dict__
-----------------------
op

('x', 'y', '__dict__')
10
100
('x', 'y', '__dict__')
{'x': 100}
10
50
{'x': 100, 'new_attr': 50}




key::->

if you declare dict in slots then you can add new attribute at run time
but it will store in dict class attribute now you can modified read onliy variables
but that variable will store in dict

"""