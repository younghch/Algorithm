# https://leetcode.com/problems/binary-tree-maximum-path-sum
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        self.max_sum_upward(root)
        return self.max_sum

    def max_sum_upward(self, node: Optional[TreeNode]) -> int:
        sum_left = 0 if node.left is None else self.max_sum_upward(node.left)  
        sum_right = 0 if node.right is None else self.max_sum_upward(node.right)  
        max_sum_upward = node.val + max(sum_left, sum_right, 0)
        sum_all = node.val + sum_left + sum_right 
        self.max_sum = max(self.max_sum, max_sum_upward, sum_all)
        return max_sum_upward

        



