class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def print_list(self):
        result = ""
        temp = self
        while temp is not None:
            result += str(temp.value) + " "
            temp = temp.next
        return result


def reverse(head):
    current = head
    previous = None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def reverse(head):
    current = head
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def reverse(head):
    current = head
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print(head.print_list())
