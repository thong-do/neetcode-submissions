class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        min = nums[0]
        
        while l <= r:
            a = (l + r)//2
            if nums[a] < min:
                min = nums[a]
                r = a
            else:
                l += 1
        return min
        