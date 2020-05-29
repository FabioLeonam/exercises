"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """ Do not return anything, modify s in-place instead."""
        
        inicio = 0
        fim = len(s) - 1
        while inicio < fim:
            s[inicio], s[fim] = s[fim], s[inicio]
            inicio += 1
            fim -=  1