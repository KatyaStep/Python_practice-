class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree, array):
    if tree.left:
        inOrderTraverse(tree.left, array)

    array.append(tree.value)

    if tree.right:
        inOrderTraverse(tree.right, array)

    return array

def preOrderTraverse(tree, array):

    array.append(tree.value)

    if tree.left:
        preOrderTraverse(tree.left, array)

    if tree.right:
        preOrderTraverse(tree.right, array)


    return array

def postOrderTraverse(tree, array):

    if tree.left:
        postOrderTraverse(tree.left, array)

    if tree.right:
        postOrderTraverse(tree.right, array)

    array.append(tree.value)

    return array




root_node = BST(10)
root_node.left = BST(5)
root_node.right = BST(15)

left_node_two = root_node.left
left_node_two.left = BST(2)
left_node_two.right = BST(5)

left_node_three = left_node_two.left
left_node_three.left = BST(1)

# left_node_four = left_node_two.right
# left_node_four.right = BST(5)

right_node_two = root_node.right
# right_node_two.left = BST(13)
right_node_two.right = BST(22)

my_array = []

# print(inOrderTraverse(root_node, my_array))
# print(preOrderTraverse(root_node, my_array))
print(postOrderTraverse(root_node, my_array))