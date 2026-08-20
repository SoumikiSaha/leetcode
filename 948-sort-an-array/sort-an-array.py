class Solution:
    def sortArray(self, nums):
        offset = 50000
        size = 100001

        count = [0] * size

        for num in nums:
            count[num + offset] += 1

        index = 0

        for value in range(size):
            while count[value] > 0:
                nums[index] = value - offset
                index += 1
                count[value] -= 1

        return nums