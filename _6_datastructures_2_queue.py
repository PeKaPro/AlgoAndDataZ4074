import time
from collections import deque


class QueueFromList:

    def __init__(self):
        self._data = []

    def put(self, element):
        self._data.append(element)

    # def put(self, element):
    #     self._data.insert(0, element)

    def get(self):
        if not self._data:
            return None
        return self._data.pop(0)

    # def get(self):
    #     if not self._data:
    #         return None
    #
    #     return self._data.pop()



my_queue = QueueFromList()

my_queue.put(1)
my_queue.put(3)
my_queue.put(7)
my_queue.put(5)

print(my_queue.get())


my_queue = QueueFromList()
t0 = time.time()
for i in range(100000):
    my_queue.put(i)
t1 = time.time()
for i in range(100000):
    my_queue.get()
t2 = time.time()

print("total time: ", t2-t0)
print("put: ", t1-t0)
print("get: ", t2-t1)



[ 2, 3, 4, 5, 8, 9, 10, 55, 100,150,20,30]



class QueueFromDeque:

    def __init__(self):
        self._data = deque()

    def put(self, element):
        self._data.append(element)

    def get(self):
        if not self._data:
            return None
        return self._data.popleft()



my_queue = QueueFromDeque()

my_queue.put(1)
my_queue.put(3)
my_queue.put(7)
my_queue.put(5)

print(my_queue.get())



my_queue = QueueFromDeque()
t0 = time.time()
for i in range(100000):
    my_queue.put(i)
t1 = time.time()
for i in range(100000):
    my_queue.get()
t2 = time.time()

print("total time: ", t2-t0)
print("put: ", t1-t0)
print("get: ", t2-t1)


"""
QueueFromDeque
total time:  0.062218427658081055
put:  0.025082826614379883
get:  0.03713560104370117

QueueFromList
total time:  7.535655498504639
put:  0.021747350692749023
get:  7.51390814781189

"""