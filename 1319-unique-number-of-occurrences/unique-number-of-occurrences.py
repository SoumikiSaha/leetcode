class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        # count frequency
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # check uniqueness
        occurrences = set(freq.values())

        return len(occurrences) == len(freq)
