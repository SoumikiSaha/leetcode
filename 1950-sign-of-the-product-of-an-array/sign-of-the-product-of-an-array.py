class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            prod *= n
        return 1 if prod >= 1 else -1 if prod < 0 else 0
        