class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def dfs(root):
    number = 0
    paths = []
    recursive_dfs(root, number, paths)
    return paths


def recursive_dfs(root, number, paths):
    if root is None:
        return
    number += root.val
    if root.left is None and root.right is None:
        paths.append(number)
    else:
        recursive_dfs(root.left, number, paths)
        recursive_dfs(root.right, number, paths)
    number -= root.val


def recursive_dfs(root, number, paths):
    if root is None:
        return
    number += root.val
    if root.left is None and root.right is None:
        paths.append(number)
    else:
        recursive_dfs(root.left, number, paths)
        recursive_dfs(root.right, number, paths)
    number -= root.val

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(dfs(root))