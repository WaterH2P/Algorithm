// 343. 整数拆分
// 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
  if (n === 2) { return 1; }
  if (n === 3) { return 2; }

  let dp = {
    4: 4,
    5: 6,
    6: 9
  };
  function maxMul(n) {
    if (n <=4 ) { return n; }
    if (dp[n]) { return dp[n]; }
    else {
      for (let i = 2; i <= Number.parseInt(n / 2); i++) {
        let max = maxMul(i) * maxMul(n - i);
        if (!dp[n] || dp[n] < max) { dp[n] = max; }
      }
      return dp[n];
    }
  }

  return maxMul(n);
};

let n = 10;
console.log(integerBreak(n));