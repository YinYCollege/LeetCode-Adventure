class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique, stack, longest = set(), [], 0
        for i in range(len(s)):
            if s[i: i + 1] in unique:
                while stack[0] != s[i: i + 1]:
                    unique.remove(stack.pop(0))
                unique.remove(stack.pop(0))
            unique.add(s[i: i + 1])
            stack.append(s[i: i + 1])
            if len(stack) > longest: longest = len(stack)
        return longest