class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for i in range(min(len(word1), len(word2))):
            ans += f'{word1[i]}{word2[i]}'
        ans += word1[min(len(word1), len(word2)):]
        ans += word2[min(len(word1), len(word2)):]
        return ans

        
