class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        for d in digits:
            digit = digit * 10 + d
        digit += 1
        return [int(_f) for _f in str(digit)]