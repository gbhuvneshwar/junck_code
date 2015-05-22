from weakref import WeakKeyDictionary


class NonNegative(object):
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %d" % value)
        self.data[instance] = value


class Movie(object):
    import pdb;pdb.set_trace()
    rating = NonNegative(0)
    budget = NonNegative(0)

    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.budget = budget
        self.runtime = runtime
        self.gross = gross

    def profit(self):
        return self.gross - self.budget

m1 = Movie('POH', 5, 12, -800, 1000)
print m1.profit()

#m1.budget = -100
#print m1.budget