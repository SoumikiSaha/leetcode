class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cur_count = 0

        for i in window:
            if i in vowels:
                cur_count += 1
        
        max_count = cur_count

        for n in range(k, len(s)):
            if s[n] in vowels:
                cur_count += 1
            if s[n-k] in vowels:
                cur_count -= 1
            max_count = max(max_count, cur_count)
        
        return max_count

        