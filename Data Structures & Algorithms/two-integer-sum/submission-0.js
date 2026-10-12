class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
       const numLen = nums.length;

  for (let i = 0; i < numLen; i++) {
    for (let j = i + 1; j < numLen; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
    }
}
