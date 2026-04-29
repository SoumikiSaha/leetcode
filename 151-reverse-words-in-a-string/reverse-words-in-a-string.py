class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split()
        l, r = 0, len(s_l)-1
        while l < r:
            s_l[l], s_l[r] = s_l[r], s_l[l]
            l += 1
            r -= 1
        return " ".join(s_l)