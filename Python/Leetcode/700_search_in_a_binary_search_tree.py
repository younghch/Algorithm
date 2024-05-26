# https://leetcode.com/problems/search-in-a-binary-search-tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        cur = root
        while cur:
            if target > cur.val:
                cur = cur.right
            elif target < cur.val:
                cur = cur.left
            else:
                break
        return cur
    
