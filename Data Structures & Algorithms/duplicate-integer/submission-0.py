class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        appeared = {}
        for i in nums:
            if i in appeared:
                return True
            else:
                appeared.update({i: 1})
        return False
         