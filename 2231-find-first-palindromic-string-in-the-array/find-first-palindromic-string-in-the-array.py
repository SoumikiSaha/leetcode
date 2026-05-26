class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # for word in words:
        #     if word == word[::-1]:
        #         return word
        # return ""

        for word in words:
            is_palindrome = True
            left = 0
            right = len(word) - 1

            while left < right:
                if word[left] != word[right]:
                    is_palindrome = False
                    break
                
                left += 1
                right -= 1
            
            if is_palindrome:
                return word
        
        return ""


        