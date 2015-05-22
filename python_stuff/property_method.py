class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        if budget < 0:
            raise ValueError("cant accept negative value for budget: % d" % budget)
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget
"""
m1 = Movie('aaa', 5, 11, 100, 300)


print m1.budget
m1.budget = -100 //this should not allowed bcz it negative value,for rectifying this we use property
print m1.budget

100
-100
"""


class Movie_1(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("value can not be negative: %d" % value)
        self._budget = value

    def profit(self):
        return self.gross - self.budget

"""
m1 = Movie_1('RDB', 5, 1, 90, 900)

#print m1.profit()

m1.budget = -90
(Traceback (most recent call last):
  File "property_method.py", line 51, in <module>
    m1.budget = -90
  File "property_method.py", line 41, in budget
    raise ValueError("value can not be negative: %d" % value)
ValueError: value can not be negative: -90
)


#print m1.profit()
"""