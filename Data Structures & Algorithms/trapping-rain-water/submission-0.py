class Solution:
    def trap(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, 1

        while l <= r and r < len(heights):
            if heights[r] >= heights[l]:
                s = heights[l] * (r - l - 1)
                for i in heights[l+1: r]:
                    s -= i
                res += s
                l = r
                r += 1
                continue
            elif heights[l] > heights[r]:
                if r == len(heights) - 1:
                    x = r - 1
                    while x >= l:
                        if heights[x] >= heights[r]:
                            s = heights[r] * (r - x - 1)
                            for i in heights[x+1: r]:
                                s -= i
                            res += s
                            r = x
                            x -= 1
                            continue
                        elif heights[x] < heights[r]:
                            x -= 1
                    break
                else:
                    r += 1
                continue

        return res