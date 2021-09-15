class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatedFromLinkedList(LinkedList):
    current_node = LinkedList

    # if current_node. next is None or current_node.next.next is None:
    #     return LinkedList
    while current_node.next.next is not None:
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        current_node = current_node.next
            # removeDuplicatedFromLinkedList(current_node.next)
    print(LinkedList)

    return LinkedList



head = LinkedList(1)
head.next = LinkedList(1)

second = head.next
second.next = LinkedList(3)

third = second.next
third.next = LinkedList(4)

fourth = third.next
fourth.next = LinkedList(4)

fifth = fourth.next
fifth.next = LinkedList(5)

sixth = fifth.next
sixth.next = LinkedList(6)


removeDuplicatedFromLinkedList(head)