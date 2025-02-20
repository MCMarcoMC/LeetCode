from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return []
                
            
nums = [2, 5,3,9,3]
target = 6


solution = Solution()
result = solution.twoSum(nums, target)
print(result)