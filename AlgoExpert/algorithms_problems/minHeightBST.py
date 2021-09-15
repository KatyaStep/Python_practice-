# O(nlog(n)) time O(n) space
def minHeightBst(array):

    """
    TODO: find root"
    TODO: left part of the tree
    TODO: right part of the tree"""

    rootValue = array[len(array)//2]
    rootNode = BST(rootValue)
    leftPart = array[:len(array) // 2]
    rightPart = array[(len(array) // 2)+1:]

    helperMethod(leftPart, rootNode)
    helperMethod(rightPart, rootNode)

    return rootNode


def helperMethod(array, currentNode):

    if len(array) >= 1:
        newValue = array[len(array)//2]
        BST.insert(currentNode, newValue)

        newArrayLeft = array[:(len(array)//2)]
        newArrayRight = array[(len(array)//2)+1:]

        helperMethod(newArrayLeft, currentNode)
        helperMethod(newArrayRight, currentNode)

    return True

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# root_node = BST(10)
# root_node.left = BST(5)
# root_node.right = BST(15)
#
# left_node_two = root_node.left
# left_node_two.left = BST(2)
# left_node_two.right = BST(5)
#
# left_node_three = left_node_two.left
# left_node_three.left = BST(1)
#
# # left_node_four = left_node_two.right
# # left_node_four.right = BST(5)
#
# right_node_two = root_node.right
# # right_node_two.left = BST(13)
# right_node_two.right = BST(22)

my_array= [1, 2, 5, 7, 10, 13, 14, 15, 22]

minHeightBst(my_array)