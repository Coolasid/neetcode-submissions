class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        is_zero_present = False
        zero_count = 0
        product = 1
        product_array = []

        # Calculate the product of nums
        for num in nums:
            if num == 0:
                is_zero_present = True
                zero_count += 1
            else:
                product *= num

        if zero_count == len(nums) or zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if is_zero_present:
                if num == 0:
                    product_array.append(product)
                else:
                    product_array.append(0)
            else:
                product_array.append(int(product/num))

        return product_array