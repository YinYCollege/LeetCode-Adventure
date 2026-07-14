class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            if len(s) - i > 1: # means atleast two more and so we can check i + 1
                if s[i] == "C":
                    if s[i + 1] == "M":
                        res += 900
                        i += 2
                        continue
                    elif s[i + 1] == "D":
                        res += 400
                        i += 2
                        continue
                elif s[i] == "X":
                    if s[i + 1] == "C":
                        res += 90
                        i += 2
                        continue
                    elif s[i + 1] == "L":
                        res += 40
                        i += 2
                        continue
                elif s[i] == "I":
                    if s[i + 1] == "X":
                        res += 9
                        i += 2
                        continue
                    elif s[i + 1] == "V":
                        res += 4
                        i += 2
                        continue
            if s[i] == "M":
                res += 1000
            elif s[i] == "D":
                res += 500
            elif s[i] == "C":
                res += 100
            elif s[i] == "L":
                res += 50
            elif s[i] == "X":
                res += 10
            elif s[i] == "V":
                res += 5
            else:
                res += 1
            i += 1
        return res