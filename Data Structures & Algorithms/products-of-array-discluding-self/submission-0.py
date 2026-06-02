class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        zero_num = 0
        for i in nums:
            if i == 0:
                zero_num += 1
                continue
            prod = prod * i

        res = []
        for i in nums:
            if zero_num > 1:
                res.append(0)
            elif zero_num == 1:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // i)

        return res