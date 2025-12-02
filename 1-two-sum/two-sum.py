class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {}
        # for i , v in enumerate(nums):
        #     if target - v in hashmap:
        #         return i, hashmap[target - v]
        #     else:
        #         hashmap[v] = i
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i , j