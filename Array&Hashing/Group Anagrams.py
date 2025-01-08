from collections import defaultdict
from typing import List

# Check the duplicate with hashtable with time O(m*n) and space O(m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[list[str]]:
        hashT = defaultdict(list)
        for string in strs:
            a = [0] * 26
            for char in string:
                a[ord(char) - ord ('a')] = 1 + a[ord(char) - ord ('a')]
            hashT[tuple(a)].append(string)
        return list(hashT.values())
