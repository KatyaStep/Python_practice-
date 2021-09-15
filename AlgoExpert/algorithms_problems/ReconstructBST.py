class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    rootNode = BST(preOrderTraversalValues[0])

    for i in range(1, len(preOrderTraversalValues)):
        traverseTree(rootNode, preOrderTraversalValues[i])

    return rootNode


def traverseTree(node, value):

    if value >= node.value:
        if node.right is None:
            node.right = BST(value)
        else:
            traverseTree(node.right, value)
    else:
        if node.left is None:
            node.left = BST(value)
        else:
            traverseTree(node.left, value)

    return node


# my_array = [10, 4, 2, 1, 5, 17, 19, 18]
# my_array = [10, 4, 2, 1, 3, 5, 6, 9, 7, 17, 19, 18]
my_array = [10, 4, 2, 1, 3, 5, 5, 6, 5, 5, 9, 7, 17, 19, 18, 18, 19]
reconstructBst(my_array)