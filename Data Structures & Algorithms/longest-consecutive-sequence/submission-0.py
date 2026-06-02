class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxScore = 0

        for i in numSet:
            if i - 1 in numSet:
                continue
            currentNum = i
            currentScore = 1
            
            while currentNum + 1 in numSet:
                currentNum += 1
                currentScore += 1
            
            maxScore = max(maxScore, currentScore)
        
        return maxScore
