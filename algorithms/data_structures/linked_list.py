'''
    Implementation of LinkedList and DoublyLinkedList
'''

class LinkedList(object):

    def __init__(self, node=None):
        self.head = node

    def appendLeft(self, node):
        if not self.head:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        while (next):
            previous = current
            next = current.next
            if next.value == value:
                if next.next:
                    previous.next = next.next
                else:
                    previous.next = None
                return

        return 'Value not found'

    def size(self):
        count = 0
        current = self.head
        while (current):
            count += 1
            current = current.next
        return count

class DoublyLinkedList(LinkedList):

    def __init__(self, node=None):
        super(LinkedList, self).__init__(node)
        self.tail = node

    def appendLeft(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def appendRight(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            self.tail.previous = temp



if __name__ == '__main__':
    from algorithms.data_structures.node import LinkedListNode
    node = LinkedListNode(1)

    linkedList = LinkedList(node)
    linkedList.appendLeft(LinkedListNode(2))
    linkedList.appendLeft(LinkedListNode(3))

    assert linkedList.head._value == 3
    assert linkedList.size() == 3
