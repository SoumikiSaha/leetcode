class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            h, n = len(haystack), len(needle)
            for i in range(h-n+1):
                if haystack[i:i+n] == needle:
                    return i
        else:
            return -1


        