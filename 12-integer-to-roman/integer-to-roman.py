class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        thousands = ((num % 10000) - (num % 1000)) // 1000
        hundreds = ((num % 1000) - (num % 100)) // 100
        tens = ((num % 100) - (num % 10)) // 10
        ones = num % 10
        while thousands:
            res += "M"
            thousands -= 1
        while hundreds:
            if hundreds == 9:
                res += "CM"
                hundreds -= 9
            elif hundreds == 4:
                res += "CD"
                hundreds -= 4
            elif hundreds >= 5:
                res += "D"
                hundreds -= 5
            else:
                res += "C"
                hundreds -= 1
        while tens:
            if tens == 9:
                res += "XC"
                tens -= 9
            elif tens == 4:
                res += "XL"
                tens -= 4
            elif tens >= 5:
                res += "L"
                tens -= 5
            else:
                res += "X"
                tens -= 1
        while ones:
            if ones == 9:
                res += "IX"
                ones -= 9
            elif ones == 4:
                res += "IV"
                ones -= 4
            elif ones >= 5:
                res += "V"
                ones -= 5
            else: 
                res += "I"
                ones -= 1
        return res