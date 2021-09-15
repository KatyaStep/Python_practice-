import NodeDepth

def test_one():
    root_node = NodeDepth.BSTNode(1)
    root_node.left = NodeDepth.BSTNode(2)
    root_node.right = NodeDepth.BSTNode(3)

    left_node_two = root_node.left
    left_node_two.left = NodeDepth.BSTNode(4)
    left_node_two.right = NodeDepth.BSTNode(5)

    left_node_three = left_node_two.left
    left_node_three.left = NodeDepth.BSTNode(8)
    left_node_three.right = NodeDepth.BSTNode(9)

    right_node_three = left_node_two.right
    # right_node_three.left = NodeDepth.BSTNode(10)

    right_node_two = root_node.right
    right_node_two.left = NodeDepth.BSTNode(6)
    right_node_two.right = NodeDepth.BSTNode(7)

    res = 16

