class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree, node):
    array = []
    getSuccessor(tree, array)
    for n in range(1, len(array)):
        if array[n-1].value == node.value:
            return array[n].value
        if array[n] == array[-1]:
            return None

def getSuccessor(tree, array):
    if tree is None:
        return

    getSuccessor(tree.left, array)
    array.append(tree)
    getSuccessor(tree.right, array)

    return array





# def helper_method(tree, node):
#     if tree is None:
#         return None
#
#     if tree.value == node.value:
#         return tree
#
#     helper_method(tree.left, node)
#     helper_method(tree.right, node)


root_node = BinaryTree(1)
root_node.left = BinaryTree(2)
root_node.right = BinaryTree(3)

left_node_two = root_node.left
left_node_two.left = BinaryTree(4)
left_node_two.right = BinaryTree(5)

left_node_three = left_node_two.left
left_node_three.left = BinaryTree(6)

# left_node_four = left_node_two.right
# left_node_four.right = BST(5)

# right_node_two = root_node.right
# right_node_two.left = BST(13)
# right_node_two.right = BinaryTree(22)

print(find_successor(root_node, left_node_two.right))