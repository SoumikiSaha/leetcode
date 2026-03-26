class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd length palindromes
            count += self.countPalindrome(s, i, i)
            # even length palindromes
            count += self.countPalindrome(s, i, i+1)
        return count

    def countPalindrome(self, word, left, right):
        count = 0
        while left >= 0 and right < len(word):
            if word[left] == word[right]:
                count += 1
            else:
                break
            left -= 1
            right += 1
        return count