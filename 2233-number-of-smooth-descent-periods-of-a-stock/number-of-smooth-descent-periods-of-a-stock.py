class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        curr_len = 0
        
        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                curr_len += 1
            else:
                curr_len = 1
            
            ans += curr_len
        
        return ans
