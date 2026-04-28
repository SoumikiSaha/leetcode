from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten the grid
        arr = [num for row in grid for num in row]
        
        # Step 2: Check feasibility (same remainder)
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort the array
        arr.sort()
        
        # Step 4: Find median
        median = arr[len(arr) // 2]
        
        # Step 5: Count operations
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations