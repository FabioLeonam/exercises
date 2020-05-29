"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pointer = head
        while pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head