# 160 . Intersection of Two Linked Lists

""" Write a program to find the the node at which the intersection of two singly linked lists begins"""
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Brute Force
""" def length_(self, head):
    lenn = 0
    while(head != None):
        lenn += 1
        head = head.next

def find_merge_point(self, head1, head2):
    m = length_(head1)
    n = length_(head2)
    head2 = b
    for i in range(m):
        b = head2
        for in range(n):
            if head1 == head2:
                return head1
            head2 = head2.next
        head1 = head1.next
 """

#2 Best option


class Solution:
    def _length(self, head):
        length_ = 0
        while(head != None):
            length_ += 1
            head = head.next
        return length_
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m = self._length(headA)
        n = self._length(headB)
        d = n - m
        
        if m > n:
            temp = headA
            headA = headB
            headB = temp
            d = m - n
            
        for i in range(d):
            headB = headB.next
        
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        

