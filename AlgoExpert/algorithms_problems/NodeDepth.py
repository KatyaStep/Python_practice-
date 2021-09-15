import math

class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    depth = 1
    result = []
    res = __impl_node_depth(root, depth)
    print(res)
    return res


def __impl_node_depth(node, depth):


    if node.left:
        depth += 1
        __impl_node_depth(node.left, depth)
    if node.right:
        depth += 1
        __impl_node_depth(node.left, depth)

    return depth



root_node = BSTNode(1)
root_node.left = BSTNode(2)
# root_node.right = BSTNode(3)

left_node_two = root_node.left
left_node_two.left = BSTNode(4)
# left_node_two.right = BSTNode(5)

left_node_three = left_node_two.left
left_node_three.left = BSTNode(8)
# left_node_three.right = BSTNode(9)

right_node_three = left_node_two.right
    # right_node_three.left = NodeDepth.BSTNode(10)

# right_node_two = root_node.right
# right_node_two.left = BSTNode(6)
# right_node_two.right = BSTNode(7)


nodeDepths(root_node)