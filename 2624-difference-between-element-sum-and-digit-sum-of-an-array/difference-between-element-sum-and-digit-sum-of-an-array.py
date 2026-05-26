class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nums_char = ''
        nums_sum = 0
        for n in nums:
            nums_char += str(n)
            nums_sum += n
        nums_char_count = 0
        for ch in nums_char:
            nums_char_count += int(ch)
        return abs(nums_sum - nums_char_count)
        


        