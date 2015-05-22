# Simple Iterator

"""
an iterator is an object which allows a programmer to traverse through all the elements of a collection,
regardless of its specific implementation.
-----------------------------
an iterator is an object which implements the iterator protocol.
The iterator protocol consists of two methods. The __iter__() method,
which must return the iterator object and the next() method,
which returns the next element from a sequence.

"""


class MyIter(object):
    def __init__(self, val):
        self.val = val
        print "Hi from init"

    def __iter__(self):
        print "Hi from iter"
        print self.__class__
        return self

    def next(self):
        print "Hi from next "
        if self.val >= 5:
            raise StopIteration
        self.val += 1
        print "Hi from next end"
        print self.val
        return self.val


i = MyIter(0)

#for j in i:
#    print j ##it will return one value every time

"""
Hi from init
Hi from iter
<class '__main__.MyIter'>
Hi from next
Hi from next end
1
1
Hi from next
Hi from next end
2
2
Hi from next
Hi from next end
3
3
Hi from next
Hi from next end
4
4
Hi from next
Hi from next end
5
5
Hi from next


"""


print list(i) #this will append all value in the list and return that list


"""
Hi from init
Hi from iter
<class '__main__.MyIter'>
Hi from next
Hi from next end
1
Hi from next
Hi from next end
2
Hi from next
Hi from next end
3
Hi from next
Hi from next end
4
Hi from next
Hi from next end
5
Hi from next
[1, 2, 3, 4, 5]

"""
