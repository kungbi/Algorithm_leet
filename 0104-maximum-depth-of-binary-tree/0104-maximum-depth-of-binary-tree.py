# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, node: TreeNode, depth) -> int:
        if node.left == None and node.right == None:
            return depth

        a = b = 0
        if node.left:
            a = self.f(node.left, depth + 1)
        if node.right:
            b = self.f(node.right, depth + 1)
        return max(a, b)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.f(root, 1)
        return 0
        