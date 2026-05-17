class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Sum of first window
        window_sum = sum(nums[:k])

        # Initialize max_sum
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):

            # Remove left element and add new right element
            window_sum = window_sum - nums[i - k] + nums[i]

            # Update max_sum
            max_sum = max(max_sum, window_sum)

        # Return maximum average
        return max_sum / k