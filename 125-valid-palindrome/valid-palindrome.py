class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = re.sub("[^a-zA-Z0-9]", "", s).lower()
        print(word)
        l , r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
        
        