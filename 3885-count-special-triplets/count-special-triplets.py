class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Build frequency map manually
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        
        left = {}   # empty initially
        ans = 0
        
        for x in nums:
            right[x] -= 1  # moving current element from right to left
            
            target = x * 2
            
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            
            ans = (ans + left_count * right_count) % MOD
            
            # Add current element to left map
            left[x] = left.get(x, 0) + 1
        
        return ans
        