class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        right_max = height[length - 1]
        left_max = height[0]

        left_max_height = [0] * length
        right_max_height = [0] * length

        right_max_height[length - 1] = right_max
        left_max_height[0] = left_max

        for i in range(1, length):
            left_max_height[i] = max(height[i - 1], left_max_height[i - 1])

        for i in range(length - 2, -1, -1):
            right_max_height[i] = max(height[i + 1], right_max_height[i + 1])

        area = 0
        for i in range(length):
            area += max(0, (min(left_max_height[i], right_max_height[i]) - height[i]))

        return area
