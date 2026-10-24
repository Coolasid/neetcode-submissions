class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        l, r = 0, length - 1
        left_max, right_max, area = 0, 0, 0

        while l < r:
            if height[l] <= height[r]:
                area += max(0, (left_max - height[l]))
                left_max = max(height[l], left_max)
                l += 1
            else:
                area += max(0, (right_max - height[r]))
                right_max = max(height[r], right_max)
                r -= 1
        return area
