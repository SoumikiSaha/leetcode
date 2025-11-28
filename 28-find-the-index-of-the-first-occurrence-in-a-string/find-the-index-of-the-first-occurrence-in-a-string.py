class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            n, m = len(haystack), len(needle)

        # Loop through haystack so that there is enough space for needle to match
            for i in range(n - m + 1):
            # Extract substring of length m and compare
                if haystack[i:i+m] == needle:
                    return i
        else:
            return -1


        