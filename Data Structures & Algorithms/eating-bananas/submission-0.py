import math

class Solution:
    def check(self, piles, rate, h):
        if rate == 0:
            return False
        totalHour = 0
        for i in piles:
            totalHour += math.ceil(i/rate)
        
        return totalHour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
    
        maxRate = piles[-1]
        
        if h == len(piles):
            return maxRate
            
        l, r = 0, 1000000000
        
        while l < r:
            a = (l + r)//2
            if self.check(piles, int(a), h):
                r = a
            else:
                l = a + 1
        
        return l