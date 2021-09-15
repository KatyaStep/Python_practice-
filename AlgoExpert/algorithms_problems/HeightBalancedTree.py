class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class heightTree:
    def __init__(self, height, difference):
        self.height = height
        self.difference = difference

def heightBalancedBinaryTree(tree):
    # Write your code here.
    # return getHeight(tree).height_right == getHeight(tree).height_left
    tree_info = getHeight(tree).difference
    return tree_info

def getHeight(tree):
    if tree is None:
        return heightTree(0, 0)

    leftTree = getHeight(tree.left)
    rightTree = getHeight(tree.right)

    height = 1 + max(leftTree.height, rightTree.height)
    difference = abs(leftTree.height - rightTree.height)

    return heightTree(height, difference)


root_node = BinaryTree(1)
root_node.left = BinaryTree(2)
root_node.right = BinaryTree(3)

left_node_two = root_node.left
left_node_two.left = BinaryTree(4)
left_node_two.right = BinaryTree(5)

left_node_three = left_node_two.right
left_node_three.left = BinaryTree(7)
left_node_three.right = BinaryTree(8)

left_node_four = left_node_three.right
left_node_four.right = BinaryTree(9)
#
right_node_two = left_node_four.right
right_node_two.right = BinaryTree(10)

right_node_three = root_node.right
right_node_three.right = BinaryTree(6)

print(heightBalancedBinaryTree(root_node))