class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest_seq = 1
        current_streak = 1

        for i in range(1, len(nums)):
            current = nums[i - 1]
            nxt = nums[i]

            if current + 1 == nxt:
                current_streak += 1
            elif current == nxt:
                continue
            else:
                longest_seq = max(longest_seq, current_streak)
                current_streak = 1

        return max(longest_seq, current_streak)
