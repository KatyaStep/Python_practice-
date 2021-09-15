class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def binaryTreeDiameter(tree):

    # helperMethod(0, tree, 0)
    if tree is None:
        return

    return 

def helperMethod(edges, node, array):



    return array


root_node = BinaryTree(1)
root_node.left = BinaryTree(3)
root_node.right = BinaryTree(2)

left_node_two = root_node.left
left_node_two.left = BinaryTree(7)
left_node_two.right = BinaryTree(4)

left_node_three = left_node_two.left
left_node_three.left = BinaryTree(8)

left_node_four = left_node_three.left
left_node_four.left = BinaryTree(9)

right_node_two = left_node_two.right
right_node_two.right = BinaryTree(5)

right_node_three = right_node_two.right
right_node_three.right = BinaryTree(6)

# right_node_two = root_node.right
# right_node_two.left = BinaryTree(13)
# right_node_two.right = BinaryTree(22)
#
# right_node_three = right_node_two.left
# # right_node_three.left = BSTNode(12)
# right_node_three.right = BinaryTree(14)
#

print(binaryTreeDiameter(root_node))