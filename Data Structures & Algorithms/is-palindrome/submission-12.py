class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([c.lower() for c in s if c.isalnum()])
        l, r = 0, len(clean) - 1
        if r == -1:
            return True
        while clean[l] == clean[r]:
            if l >= r :
                return True
            l += 1
            r -= 1
        
        return False
