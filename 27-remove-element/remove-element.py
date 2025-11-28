class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [_f for _f in nums if _f != val]
        return len(nums)