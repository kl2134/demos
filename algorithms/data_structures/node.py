class BaseNode(object):

    def __init__(self, value):
        self.value = value

class GraphNode(BaseNode):

    def __init__(self, value):
        BaseNode.__init__(self, value)
        self.neighbors = []

class LinkedListNode(object):

    def __init__(self, value):
        BaseNode.__init__(self, value)
        self.next = None

class BinaryTreeNode(BaseNode):

    def __init__(self, value, left=None, right=None):
        BaseNode.__init__(self, value)
        self.left = left
        self.right = right

if __name__ == '__main__':

    baseNode = BaseNode(1)
    assert baseNode.value == 1

    gNode = GraphNode(1)
    assert gNode.value == 1
    assert gNode.neighbors == []

    llNode = LinkedListNode(1)
    assert llNode.value == 1
    assert llNode.next == None

    tNode = BinaryTreeNode(1)
    assert tNode.value == 1
    assert tNode.left == None
    assert tNode.right == None


