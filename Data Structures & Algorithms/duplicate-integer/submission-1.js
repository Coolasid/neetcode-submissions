class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
          const numsLen = nums.length;
  const numsObj = {};
  for (let i = 0; i < numsLen; i++) {
    numsObj[nums[i]] =
      numsObj[nums[i]] === undefined ? 1 : numsObj[nums[i]] + 1;
  }

  const values = Object.values(numsObj);

  for (const count of values) {
    if (count > 1) {
      return true;
    }
  }
  return false;
    }
}
