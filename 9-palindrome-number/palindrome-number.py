class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x2, temp = 0, x
        while temp > 0:
            x2 *= 10
            x2 += temp % 10
            temp //= 10
        return x == x2