class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for spell in spells:
            left, right = 0, m-1
            while left <= right:
                mid = left + (right-left)//2

                if potions[mid] * spell >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(m - left)
        
        return ans
        