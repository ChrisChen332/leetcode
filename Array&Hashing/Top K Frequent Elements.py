
import heapq
from typing import List

#Using heap and hash table to solve the problem with time O(nlogk) space O(n + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashT = {}
        for num in nums:
            hashT[num] = 1 + hashT.get(num, 0)
        pq = []
        for num in hashT.keys():
            heapq.heappush(pq, (hashT[num], num))
            if len(pq) > k:
                heapq.heappop(pq)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans
    
#Solution with time O(n) space O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashT = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashT[num] = 1 + hashT.get(num, 0)
        
        for num, count in hashT.items():
            freq[count].append(num)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans