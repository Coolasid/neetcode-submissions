class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_str = [ele.lower() for ele in s if ele.isalnum()]

        left = 0
        right = len(filtered_str) - 1

        while left < right:
            if filtered_str[left] != filtered_str[right]:
                return False
            left += 1
            right -= 1

        return True
