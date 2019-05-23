class BaseNode(object):

    def __init__(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

class GraphNode(BaseNode):

    def __init__(self, value):
        BaseNode.__init__(self, value)
        self._neighbors = []

    def getNeighbors(self):
        return self._neighbors

    def addNeighbor(self, neighbor):
        if not neighbor in self._neighbors:
            self._neighbors.append(neighbor)

    def deleteNeighbor(self, neighbor):
        if neighbor in self._neighbors:
            self._neighbors.remove(neighbor)

class LinkedListNode(BaseNode):

    def __init__(self, value):
        BaseNode.__init__(self, value)
        self.next = None

class BinaryTreeNode(BaseNode):

    def __init__(self, value, left=None, right=None):
        BaseNode.__init__(self, value)
        self.left = left
        self.right = right

class DoublyLinkedListNode(LinkedListNode):

    def __init__(self, value):
        LinkedListNode.__init__(self, value)
        self.previous = None

if __name__ == '__main__':

    baseNode = BaseNode(1)
    assert baseNode._value == 1
    assert baseNode.getValue() == 1
    baseNode.setValue(2)
    assert baseNode.getValue() == 2

    gNode = GraphNode(1)
    assert gNode._value == 1
    assert gNode._neighbors == []
    assert gNode.getNeighbors() == []

    gNode.addNeighbor(34)
    assert gNode.getNeighbors() == [34]

    gNode.deleteNeighbor(3)
    assert gNode.getNeighbors() == [34]

    gNode.deleteNeighbor(34)
    assert gNode.getNeighbors() == []

    llNode = LinkedListNode(1)
    assert llNode._value == 1
    assert llNode.next == None

    dllNode = DoublyLinkedListNode(1)
    assert dllNode._value == 1
    assert dllNode.next == None
    assert dllNode.previous == None

    tNode = BinaryTreeNode(1)
    assert tNode._value == 1
    assert tNode.left == None
    assert tNode.right == None


