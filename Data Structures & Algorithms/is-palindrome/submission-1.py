class Solution:
    def isPalindrome(self, s: str) -> bool:

        def alphaNum(c):
            if (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            ):
                return True
            return False

        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left]
            right_char = s[right]

            if not alphaNum(left_char):
                left += 1
                continue
            if not alphaNum(right_char):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
