"""
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        prev = None
        current = head
        while current:
            if current.val == val:
                if prev and head:
                    prev.next = current.next #1
                    current = prev.next
                else:
                    head = head.next
                    current = head
            else:
                prev = current
                current = current.next
            
        return head