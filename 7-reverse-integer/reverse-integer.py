class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            res *= 10
            res += x % 10
            x //= 10
        if sign * res > pow(2, 31) - 1 or sign * res < -1 * pow(2, 31):
            return 0
        return sign * res