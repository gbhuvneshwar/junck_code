"""
A generator is a special routine that can be used to control the iteration behaviour of a loop.
A generator is similar to a function returning an array. A generator has parameters,
it can be called and it generates a sequence of numbers.
But unlike functions, which return a whole array, a generator yields one value at a time. This requires less memory.

>>Generators in Python:

    Are defined with the def keyword
    Use the yield keyword
    May use several yield keywords
    Return an iterator


>>Now it is important to understand, how actually the yield keyword works.
It exits the generator and returns a value. Next time the next() function of an iterator is called,
we continue on the line following the yield keyword. Note that the local variables are preserved throughout the iterations.
When there is nothing left to yield, a StopIteration exception is raised.


>>The yield enables a function to comeback where it left off when it is called again

>>The yield suspends the function and sends a value back to the caller
while retains enough state to enable the function immediately after the last yield run.
This allows the generator function to produce a series of values over time
rather than computing them all at once and sending them back in a list



>>
The primary difference between generator and normal functions is that
a generator yields a value, rather than returns a value.
The yield suspends the function and sends a value back to the caller
while retains enough state to enable the function immediately
after the last yield run. This allows the generator function to produce a series of values over time
rather than computing them all at once and sending them back in a list.

"""


def gen():
    x, y =1, 2
    yield x, y
    x += 1
    yield x, y


#g1 = gen()

#print g1.next()
#print g1.next()


"""
(1, 2)
(2, 2)

"""

#print list(g1)

"""
[(1, 2), (2, 2)]

"""

#Generater Expressions

#l1 = (x for x in range(10))
#print l1
#<generator object <genexpr> at 0xb76ddb6c>
#print l1.next()
#print l1.next()
#0
#1
#print list(l1)

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def G():
    while True:
        val = yield
        yield val*10

#g1 = G()
#print g1.next()
#print g1.send(10)
#None
#100


def G1(v1):
    while True:
        v1 *=10
        v1 = yield v1
        #yield


f1 = G1(10)

print f1.send(None)
print f1.send(11)
print f1.send(111)