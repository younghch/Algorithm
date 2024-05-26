# https://leetcode.com/problems/delete-node-in-a-bst
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNodeRecurssive(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNodeRecurssive(root.left, key)
        elif root.val < key:
            root.right = self.deleteNodeRecurssive(root.right, key)
        else:
            if root.left and root.right:                
                right_minimum = root.right                
                while right_minimum.left:
                    right_minimum = right_minimum.left
                root.val = right_minimum.val
                root.right = self.deleteNode(root.right, right_minimum.val)            
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        parent = None
        to_delete = None
        is_left = False

        while cur:
            if cur.val == key:
                to_delete = cur
                break
            parent = cur
            if key > cur.val:
                cur = cur.right
                is_left = False
            else:
                cur = cur.left
                is_left = True

        if to_delete:
            target = None
            if to_delete.left and to_delete.right:
                left_has_subtree = has_subtree(to_delete.left)
                right_has_subtree = has_subtree(to_delete.right)
                if right_has_subtree:
                    left_most = to_delete.right
                    left_most_parent = None
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left
                    if left_most_parent:
                        left_most_parent.left = left_most.right
                        left_most.right = to_delete.right
                    left_most.left = to_delete.left
                    target = left_most
                elif left_has_subtree:
                    right_most = to_delete.left
                    right_most_parent = None
                    while right_most.right:
                        right_most_parent = right_most
                        right_most = right_most.right
                    if right_most_parent:
                        right_most_parent.right = right_most.left
                        right_most.left = to_delete.left
                    right_most.right = to_delete.right
                    target = right_most
                else:
                    target = to_delete.right
                    target.left = to_delete.left
            elif to_delete.left:
                target = to_delete.left
            elif to_delete.right:
                target = to_delete.right
            else:
                target = None
            
            if parent:
                if is_left:
                    parent.left = target
                else:
                    parent.right = target
            else:
                root = target

        return root


def has_subtree(node: TreeNode):
    return node.left or node.right
    
def search_node(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    cur = root
    while cur:
        if target > cur.val:
            cur = cur.right
        elif target < cur.val:
            cur = cur.left
        else:
            break
    return cur
