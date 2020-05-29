"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Examples:
Input: 1->2->2->1
Output: true
------------------
Input: 1->2
Output: false
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
            
        tail = self.reverse_ll(slow)
        
        while tail:
            if tail.val != head.val:
                return False
            head = head.next
            tail = tail.next
        return True
        
      