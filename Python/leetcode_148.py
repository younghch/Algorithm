""""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
from typing import *
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        nodes = collections.defaultdict(list)
        node = head
        while node is not None:
            nodes[node.val].append(node)
            node = node.next
        sorted_list = sorted(nodes.items())
        head = sorted_list[0][1].pop(0)
        node = head
        for _, node_list in sorted_list:
            for cur in node_list:
                node.next = cur
                node = cur
        node.next = None
        return head

    #Merge sort

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


    def sortList2(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)