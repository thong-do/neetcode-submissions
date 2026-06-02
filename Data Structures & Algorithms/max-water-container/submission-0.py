class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = min(heights[0], heights[-1])
        width = len(heights) - 1
        max_area = high * width

        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            max_area = max(max_area, h * w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area