"""
206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
        
        """
        current  = head
        prev = None
        while current:
            prox = current.next
            current.next = prev
            prev = current
            current = prox
        return prev

        """