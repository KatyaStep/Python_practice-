class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def branchSums(root):
    cur_sum = 0
    branch_sum = []
    __impl_branch_sum(root, cur_sum, branch_sum)

    print(branch_sum)
    return branch_sum


def __impl_branch_sum(node, cur_sum, branch_sum):
    cur_sum += node.value
    if node.left:
        # print(root.left.value)
        __impl_branch_sum(node.left, cur_sum, branch_sum)
    if node.right:
        __impl_branch_sum(node.right, cur_sum, branch_sum)

    if node.left is None and node.right is None:
        branch_sum.append(cur_sum)

    return branch_sum



root_node = BSTNode(1)
root_node.left = BSTNode(2)
root_node.right = BSTNode(3)

left_node_two = root_node.left
left_node_two .left = BSTNode(4)
left_node_two .right = BSTNode(5)

left_node_three = left_node_two.left
left_node_three.left = BSTNode(8)
left_node_three.right = BSTNode(9)

right_node_three = left_node_two .right
right_node_three.left = BSTNode(10)


right_node_two = root_node.right
right_node_two.left = BSTNode(6)
right_node_two.right = BSTNode(7)


branchSums(root_node)