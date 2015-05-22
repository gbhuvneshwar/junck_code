# Dynamic Class Method Addition
def fn(self):
    print "Hi"
    return id(self), self, type(self)


class A1(object):

    def method_a(self):
        return id(self), self, type(self)


instance_1 = A1()
"""
instence_1 = A1()
print instence_1.method_a()

setattr(A1, 'method_b', fn)

print instence_1.method_b()

----------------------------
(3077974444L, <__main__.A1 object at 0xb77629ac>, <class '__main__.A1'>)
Hi
(3077974444L, <__main__.A1 object at 0xb77629ac>, <class '__main__.A1'>)

"""


# Dynamic Instance Method Addition
#If you want to add method in particular instance then::


from type import Methodtype

instance_2 = A1()


setattr(instence_1, fn.__name__, Methodtype(fn.instance1, type(instance_1)))

