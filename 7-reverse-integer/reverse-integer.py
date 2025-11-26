class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31 

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        rev = 0

        while x != 0:
            pop = x % 10
            x = x // 10

            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            
            rev = rev * 10 + pop

        return sign * rev