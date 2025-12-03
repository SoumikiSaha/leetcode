class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for position of next unique element
        k = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:   # Found new unique element
                nums[k] = nums[i]
                k += 1
        
        return k
