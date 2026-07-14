class Solution:
    def myAtoi(self, s: str) -> int:
        i, neg, res = 0, 1, 0
        while i < len(s) and s[i] == " ": # removes all whitespaces
            i += 1
        if i < len(s) and s[i] == "-": # conditional to check whether pos or neg and increment
            neg = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        while i < len(s) and s[i].isdigit(): # adds num if num else none
            res *= 10
            res += int(s[i])
            i += 1
        res = neg * res
        res = pow(2, 31) - 1 if res > pow(2, 31) - 1 else -1 * pow(2, 31) if res < -1 * pow(2, 31) else res
        return res