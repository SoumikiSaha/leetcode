# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         # digit = 0
#         # for d in digits:
#         #     digit = digit * 10 + d
#         # digit += 1
#         # return [int(_f) for _f in str(digit)]
#         if digits[-1] < 9:
#             digits[-1] += 1
        
#         return digits
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        # Start from the last digit
        while i >= 0:
            if digits[i] < 10 - 1:   # If digit < 9
                digits[i] += 1
                return digits
            digits[i] = 0           # If digit == 9, set to 0 and carry over
            i -= 1

        # If all digits were 9 (e.g., 999 → 000), add 1 at beginning
        return [1] + digits
