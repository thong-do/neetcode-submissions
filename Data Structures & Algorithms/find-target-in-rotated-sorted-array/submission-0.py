class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        min = 0
        
        while l <= r:
            a = (l + r)//2
            if nums[a] < nums[min]:
                min = a
                r = a
            else:
                l += 1
                
        if min == 0:
            l, r = 0, len(nums) - 1
        else:
            if target >= nums[min] and target <= nums[-1]:
                l, r = min, len(nums) - 1
            else:
                l, r = 0, min
                
        while l <= r:
            a = (l + r)//2
            if nums[a] == target:
                return a
                
            if nums[a] > target:
                r -= 1
            else:
                l += 1

        return -1