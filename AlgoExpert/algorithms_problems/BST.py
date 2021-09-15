
class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        current_node = self

        while current_node is not None:
            if value >= current_node.value:
                if current_node.right is None:
                    current_node.right = BSTNode(value)
                    print("Inserting value right:", current_node.right.value)
                    break
                else:
                    current_node = current_node.right

            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = BSTNode(value)
                    print("Inserting value left:", current_node.left.value)
                    break
                else:
                    current_node = current_node.left

        return self


    def contains(self, value):

        current_node = self

        while current_node is not None:
            if value == current_node.value:
                return True
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

        return False

    def remove(self, value):
        current_node = self
        parent = None

        # search for a key in BST and set its parent pointer
        while current_node and current_node.value != value:
            parent = current_node

            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right


        if current_node is None:
            return self


        # if a node is a root
        if parent is None and current_node.right:
            successor = getMinimumKey(current_node.right, "left")
            val = successor.value
            current_node.remove(successor.value)
            current_node.value = val
            return self

        elif parent is None and current_node.right is None:
            successor = getMinimumKey(current_node.left, "right")
            val = successor.value
            current_node.remove(successor.value)
            current_node.value = val

            return self

        # if a node that we want to delete doesn't have children:

        if current_node.left is None and current_node.right is None:
            if current_node != self.value:
                if parent.left == current_node:
                    parent.left = None
                else:
                    parent.right = None

        # if a node has  two children
        elif current_node.left and current_node.right:
            if current_node.value == current_node.right.value:
                current_node.right = None
                return self
            else:
                min_1 = getMinimumKey(current_node.right, "left")
                min_2 = getMinimumKey(current_node.left, "right")
                successor = min_1 if min_1.value < min_2.value else min_2
                val = successor.value
                current_node.remove(successor.value)

                current_node.value = val

        # if a node has one child
        elif current_node.left or current_node.right:
            if current_node.left:
                child = current_node.left
            else:
                child = current_node.right

            if current_node != self:
                if current_node == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self = child

            # val = successor.value
            # current_node.remove(successor.value)
            #
            # current_node.value = val

        return self


def getMinimumKey(current_node, branch):
    if branch == "right":
        if current_node.left:
            while current_node.left:
                   current_node = current_node.left
    else:
        if current_node.right:
            while current_node.right:
                   current_node = current_node.right

    return current_node


root_node = BSTNode(10)
# root_node.left = BSTNode(5)
# root_node.right = BSTNode(15)
#
# left_node_two = root_node.left
# left_node_two .left = BSTNode(2)
# left_node_two .right = BSTNode(5)
#
# left_node_three = left_node_two.left
# left_node_three.left = BSTNode(1)
#
# right_node_two = root_node.right
# right_node_two.left = BSTNode(13)
# right_node_two.right = BSTNode(22)
#
# right_node_three = right_node_two.left
# # right_node_three.left = BSTNode(12)
# right_node_three.right = BSTNode(14)

def foo(my_root_node):
    current_node = my_root_node
    while current_node is not None:
        # print(current_node.value)
        current_node = current_node.right


# root_node.insert(2)
# root_node.insert(3)
# root_node.insert(4)
# root_node.insert(5)
# root_node.insert(6)
# root_node.insert(7)
# root_node.insert(8)
# root_node.insert(9)
# root_node.insert(10)
# root_node.insert(11)
# root_node.insert(12)
# root_node.insert(13)
# root_node.insert(14)
# root_node.insert(15)
# root_node.insert(16)
# root_node.insert(17)
# root_node.insert(18)
# root_node.insert(19)
# root_node.insert(20)
# root_node.insert(13)
# root_node.insert(12)
# root_node.insert(22)
# print(root_node.contains(5))
# root_node.remove(2)
# root_node.remove(4)
# root_node.remove(6)
# root_node.remove(8)
# root_node.remove(11)
# root_node.remove(13)
# root_node.remove(15)
# root_node.remove(17)
# root_node.remove(19)
# root_node.insert(1)
# root_node.insert(2)
# root_node.insert(3)
# root_node.insert(4)
# root_node.insert(5)
# root_node.insert(6)
# root_node.insert(7)
# root_node.insert(8)
# root_node.insert(9)
# root_node.insert(10)
print(root_node.contains(9000))
# print(root_node.contains(12))
# root_node.insert(10)
root_node.insert(15)
root_node.insert(5)
root_node.insert(2)
root_node.insert(5)
root_node.insert(1)
root_node.remove(5)
# print(root_node.contains(1))
# foo(root_node)
#
# print(root_node.contains(11))
