
from typing import Optional


class Node:

    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: int):
        node = Node(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        end_node = self.tail

        node = self.head
        while node is not None:
            if node.next is not end_node:
                node = node.next
            else:
                break
        node.next = None
        self.tail = node
        return end_node.value

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        return "->".join([str(node) for node in self])








if __name__ == '__main__':

    ll = LinkedList()
    print(ll.head)
    print(ll.tail)

    ll.append(5)
    print(ll.head)
    print(ll.tail)

    ll.append(10)
    print(ll.head)
    print(ll.tail)

    ll.append(15)
    print(ll.head)
    print(ll.tail)

    print(ll.pop())
    print(ll.tail.next)
    ll.tail

    for element in [1,2,3,0]:
        print(element)

    for node in ll:
        print(node)

    ll.append(155)
    ll.append(168)

    for node in ll:
        print(node)

    print(ll)