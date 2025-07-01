class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def traverse(root):
    result = []

    if root is None:
        return result

    queue = []
    queue.append(root)
    current_level = []

    while len(queue) > 0:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop()
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    result.append(current_level)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)

print(traverse(root))

from collections import deque

def traverse(head):
    result = []

    if head is None:
        return result

    queue = deque()
    queue.append(head)

    while len(queue) != 0:
        len_curr_level = len(queue)
        curr_level = []
        for i in range(len_curr_level):
            node = queue.popleft()
            curr_level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(curr_level)
    return result


def traverse(head):
    result = []
    if head is None:
        return result

    queue = deque()
    queue.append(head)

    while len(queue) != 0:
        len_curr_level = len(queue)
        curr_level = []

        for i in range(len_curr_level):
            node = queue.popleft()
            curr_level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(curr_level)
    return result



def traverse(root):
    result = []
    if root is None:
        return []

    queue = deque()
    queue.append(root)


    while len(queue) != 0:
        curr_level_len = len(queue)
        current_level = []

        for i in range(curr_level_len):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(current_level)
    return result



