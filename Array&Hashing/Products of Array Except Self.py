from typing import List

# Bruceforcing solution with time O(n^2) space O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resL = []
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if i != j:
                    res *= nums[j]
            resL.append(res)
        return resL

# Solution with time O(n) space O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        res = [1]*len(nums)
        for i  in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums [i - 1]
        for i  in range(len(nums) - 2, - 1, -1):
            postfix[i] = postfix[i + 1] * nums [i + 1]
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i] 
        return res
            