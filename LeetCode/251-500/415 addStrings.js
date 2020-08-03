// 415. 字符串相加
// 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
// 注意：
// num1 和num2 的长度都小于 5100.
// num1 和num2 都只包含数字 0-9.
// num1 和num2 都不包含任何前导零。
// 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
  if (num1.length < num2.length) num1 = Array(num2.length - num1.length).fill(0).join('') + num1;
  else if (num1.length > num2.length) num2 = Array(num1.length - num2.length).fill(0).join('') + num2;

  let up = 0;
  let sum = Array(num1.length);
  for (let i = num1.length - 1; i >= 0; i--) {
    n1 = num1[i].charCodeAt() - 48;
    n2 = num2[i].charCodeAt() - 48;
    let res = n1 + n2 + up;
    up = res >= 10 ? 1 : 0;
    res %= 10;
    sum[i] = String.fromCharCode(res + 48);
  }
  return up === 0 ? sum.join('') : 1 + sum.join('');
};