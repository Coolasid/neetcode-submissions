class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t){
  const sLen = s.length;
  const tLen = t.length;
  if (sLen !== tLen) return false;

  const sortedS = s.split("").sort();
  const sortedT = t.split("").sort();

  for (const key in sortedS) {
    if (sortedS[key] !== sortedT[key]) {
      return false;
    }
  }
  return true;
};
}
