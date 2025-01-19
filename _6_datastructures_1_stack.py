

class StackFromList:

    def __init__(self):
        self._data = []

    def push(self, element):
        self._data.append(element)

    def pop(self):
        # element = self._data[-1]
        # del self._data[-1]
        # return element
        if not self._data:
            return None
        return self._data.pop()


#
# my_list = [1,2,3,1]
# element = my_list[-1]
# del my_list[-1]
# element
#
# print(my_list)
#
#
# my_list.pop()


my_stack = StackFromList()
my_stack.push(5)
my_stack.push(5)
my_stack.push(8)
my_stack.push(12)
print(my_stack.pop())
