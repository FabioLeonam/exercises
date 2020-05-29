"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []
        for character in address:
            if character.isdigit():
                result.append(character)
            else:
                result.append("[.]")
                
        return "".join(result)