class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charMap = {}
        maxLength = 0

        for r in range(len(s)):
            if s[r] in charMap:
                l = max(l, charMap[s[r]] + 1)

            charMap[s[r]] = r
            maxLength = max(maxLength, r - l + 1)

        return maxLength

        