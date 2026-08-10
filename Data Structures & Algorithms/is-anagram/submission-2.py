class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapa, mapb = [0] * 26, [0] * 26
        for i in range(len(s)):
            mapa[ord(s[i]) - 97] += 1
            mapb[ord(t[i]) -97] += 1

        for i in range(len(mapa)):
            if mapa[i] != mapb[i]:
                return False

        return True