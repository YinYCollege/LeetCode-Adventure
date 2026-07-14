class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        longest = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < len(res): res = res[0: len(strs[i])]
            while res != strs[i][0: len(res)]:
                res = res[0: len(res) - 1]
        return res