class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_length = 0
        l = 0
        seen_chars = set()

        for r in range(length):
            # While the current character is a duplicate, shrink from the left
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l += 1

            # Add the current character and update max length
            seen_chars.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
