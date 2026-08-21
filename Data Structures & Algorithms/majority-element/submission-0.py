class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appreared = {}

        for i in nums:
            appreared[i] = appreared.get(i, 0) + 1

        print(appreared)

        for k, v in appreared.items():
            if v > len(nums)/2:
                return k
