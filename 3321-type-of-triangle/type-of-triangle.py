class Solution:
    def triangleType(self, nums: List[int]) -> str:

        nums.sort()

        # Check triangle validity
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        unique = len(set(nums))

        if unique == 1:
            return "equilateral"

        elif unique == 2:
            return "isosceles"

        else:
            return "scalene"