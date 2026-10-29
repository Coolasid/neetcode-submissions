class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            # 1. Add incoming character to our frequency map
            count[s[r]] = count.get(s[r], 0) + 1

            # 2. Update the highest frequency seen in any window so far
            max_freq = max(max_freq, count[s[r]])

            # 3. If the characters we need to replace exceed k, shrink from the left
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # 4. Record the maximum valid window length
            max_length = max(max_length, r - l + 1)

        return max_length
