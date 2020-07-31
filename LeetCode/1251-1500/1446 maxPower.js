// 1446. 连续字符
// 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
// 请你返回字符串的能量。

/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
  let pre = s[0];
  let len = 1, maxLen = 1;
  for (let i = 1; i < s.length; i ++) {
    let char = s[i];
    if (char === pre) { len += 1; }
    else {
      if (len > maxLen) { maxLen = len; }
      if (maxLen >= s.length - i) { break; }
      pre = char;
      len = 1;
    }
  }
  if (len > maxLen) { maxLen = len; }
  return maxLen;
};