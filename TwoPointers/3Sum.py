from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        ans = []
        nums.sort()  #Use Selection or insertion

        while i < len(nums) - 2: 
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:  
                    ans.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif three_sum < 0: 
                    left += 1
                else: 
                    right -= 1

            i += 1

        return ans