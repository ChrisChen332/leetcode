class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashT = {}
        st = 0
        ans = 0
        end = 0
        maxC = 0
        while end < len(s):
            hashT[s[end]] = 1 + hashT.get(s[end], 0)
            maxC = max(hashT[s[end]], maxC)
            while end - st + 1 - maxC > k:
                hashT[s[st]] -= 1
                st += 1
            ans = max(ans, end - st + 1)
            end += 1
        return ans