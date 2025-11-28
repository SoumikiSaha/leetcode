class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
        # Loop through haystack so that there is enough space for needle to match
            for i in range(len(haystack) - len(needle) + 1):
            # Extract substring of length m and compare
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1


        