class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        for i in accounts:
            most = max(most, sum(i))
        return most
        