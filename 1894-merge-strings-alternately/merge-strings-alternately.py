class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i, j = 0, 0

        while i<len(word1) and j<len(word2):
            ans += f'{word1[i]}{word2[j]}'
            i += 1
            j += 1
        ans += f'{word1[i : ]}'
        ans += f'{word2[j : ]}'

        return ans



        
