class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, max_len = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1, l + 1, r - 1  # length, new left, new right

        for i in range(len(s)):
            # Odd palindrome
            len1, l1, r1 = expand(i, i)
            # Even palindrome
            len2, l2, r2 = expand(i, i + 1)

            # Pick the longer one
            if len1 > max_len:
                max_len = len1
                start = l1
            if len2 > max_len:
                max_len = len2
                start = l2

        return s[start:start + max_len]
