class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashS = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashS:
                hashS.remove(s[l])
                l += 1
            hashS.add(s[r])
            ans = max(ans, r - l + 1)
        return ans