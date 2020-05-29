"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: true
----------------
Input: head = [1], pos = -1
Output: false
----------------
Input: head = [1,2], pos = 0
Output: true
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        else:
            fast = head.next
            slow = head

            while fast != None and fast.next != None and slow != None:
                if fast == slow :
                    return True
                fast = fast.next.next
                slow = slow.next 
            return False
        