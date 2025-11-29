class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        med = []
        median = 0
        if len(nums) % 2 == 0:
            med = nums[len(nums)//2 - 1 : len(nums)//2 + 1]
            median = sum(med)/2
        else:
            median = float(nums[len(nums)//2]) 
        return median
        