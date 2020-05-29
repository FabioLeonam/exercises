"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.

Example: Input: nums = [12,345,2,6,7896]
         Output: 2
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            count = 0
            while num > 0:
                num //=10
                count += 1
            if count %2 == 0:
                result +=1
        
        return result