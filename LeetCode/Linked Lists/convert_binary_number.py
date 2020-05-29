"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example: 
Input: head = [1,0,1]
Output: 5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        i = 0
        result = 0
        while len(stack):
            result += stack.pop()*2**i
            i += 1
        return result