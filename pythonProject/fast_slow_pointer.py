class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def slow_fast_pointer(head):
    slow_pointer = head
    fast_pointer = head.next.next

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False

def slow_fast_pointer(head):
    slow_pointer = head
    fast_pointer = head.next.next
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False


def slow_fast_pointer(head):
    slow_pointer = head
    fast_pointer = head.next.next
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next
# head.next.next.next.next.next = Node(6)

print(slow_fast_pointer(head))