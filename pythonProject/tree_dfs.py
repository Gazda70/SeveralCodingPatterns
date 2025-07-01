class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None


def dfs_sum(root, sum):
    if not root:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return dfs_sum(root.right, sum - root.val) or dfs_sum(root.left, sum - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(dfs_sum(root, 23))


def pathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: List[List[int]]
    """

    paths = []
    pathSumRecur(root, targetSum, [], paths)
    return paths

import copy
def pathSumRecur(root, targetSum, path, paths):
    if root is None:
        return
    path.append(root.val)
    if root.val == targetSum and root.left is None and root.right is None:
        paths.append(copy.deepcopy(path))
    else:
        pathSumRecur(root.right, targetSum - root.val, path, paths)
        pathSumRecur(root.left, targetSum - root.val, path, paths)
    path.pop(0)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(pathSum(root, 23))
