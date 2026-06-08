class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,value in enumerate(nums):
            sub = target - nums[i]
            if sub in temp:
                return [temp[sub],i]
            temp[value] = i