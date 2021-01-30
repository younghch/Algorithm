"""
Invert a binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def swap_two(cur):
            if cur is None:
                return
            cur.left, cur.right = cur.right, cur.left
            swap_two(cur.left)
            swap_two(cur.right)

        swap_two(root)
        return root