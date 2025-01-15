class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tCount = {}
        sWindow = {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount) 
        ans, ansLen = [0, 0], float('inf')   
        st = 0
        for end in range(len(s)):
            sWindow[s[end]] = 1 + sWindow.get(s[end], 0)

            if s[end] in tCount and sWindow[s[end]] == tCount[s[end]]:
                have += 1
            
            while have == need:
                if (end - st + 1) < ansLen:
                    ans = [st, end]
                    ansLen = end - st + 1
                
                sWindow[s[st]] -= 1
                if s[st] in tCount and sWindow[s[st]] < tCount[s[st]]:
                    have -= 1
                st += 1
                
        return s[ans[0]:ans[1] + 1] if ansLen != float('inf') else ""