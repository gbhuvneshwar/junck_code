class C(object):
    def __init__(self, a1):
        self.setx(a1)

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    x = property(getx, setx)


c1 = C(100)
print c1.x

c1.x = 999

print c1.x

"""
100
999

@property and  x = property(getx, setx)
both are same but in python only one way to do so we use @property
"""

