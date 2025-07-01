from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.appendleft(root)
    current_level = []
    while len(queue) > 0:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
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
root.right.right = TreeNode(5)

print(traverse(root))


def traverse1(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.appendleft(root)

    while len(queue) > 0:
        current_level = []
        current_level_length = len(queue)
        for i in range(current_level_length):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(current_level)

    return result


print(traverse1(root))


def levelOrderBottom(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    result = []
    queue = []
    queue.append(root)

    while len(queue) > 0:
        current_level = []
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(current_level)

    result.reverse()

    return result

levelOrderBottom(root)