class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        org = num

        while num:
            d = num % 10
            if org % d == 0:
                count += 1
            num //=10
        return count
        