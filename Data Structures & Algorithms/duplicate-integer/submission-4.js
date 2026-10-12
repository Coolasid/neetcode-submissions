class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
         const sortedNums = nums.sort((a, b) => a - b);
  for (let key in sortedNums) {
    if (
      sortedNums[key] === sortedNums[key - 1] ||
      sortedNums[key] === sortedNums[key + 1]
    ) {
      return true;
    }
  }
  return false;
    }
}
