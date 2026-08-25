class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        num = 1
        while num * k in nums_set:
            num += 1
        return num * k
        