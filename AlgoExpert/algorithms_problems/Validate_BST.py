class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    max_value = float("inf")
    min_value = float("-inf")

    return __implValidation(tree, min_value, max_value)


def __implValidation(tree, min_value, max_value):

    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    isLeftValid = __implValidation(tree.left, min_value, tree.value)
    isRightValid = __implValidation(tree.right, tree.value, max_value)

    return isRightValid and isLeftValid





root_node = BST(10)
root_node.left = BST(5)
root_node.right = BST(15)

left_node_two = root_node.left
left_node_two.left = BST(2)
left_node_two.right = BST(5)

left_node_three = left_node_two.left
left_node_three.left = BST(1)

left_node_four = left_node_two.right
left_node_four.right = BST(11)

right_node_two = root_node.right
# right_node_two.left = BST(13)
right_node_two.right = BST(22)

# right_node_three = right_node_two.left
# # right_node_three.left = BSTNode(12)
# right_node_three.right = BST(14)

print(validateBst(root_node))
