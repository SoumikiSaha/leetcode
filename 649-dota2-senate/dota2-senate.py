class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = [], []
        for i in range(n):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        r, d = 0, 0
        while r < len(radiant) and d < len(dire):
            if radiant[r] < dire[d]:
                radiant.append(radiant[r]+n)
            else:
                dire.append(dire[d]+n)
            r += 1
            d += 1
        if r < len(radiant):
            return "Radiant"
        return "Dire"
        