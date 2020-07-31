// 剑指 Offer 47. 礼物的最大价值
// 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
// 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxValue = function(grid) {
  const m = grid.length;
  const n = grid[0].length;

  let dp = {};
  const dpKey = (x = 0, y = 0) => `${x},${y}`;
  dp[dpKey(m - 1, n - 1)] = grid[m - 1][n - 1];

  function midMaxValue (x = 0, y = 0) {
    let key = dpKey(x, y);
    if (dp[key]) { return dp[key]; }
    else {
      let r = 0, d = 0;
      if (x < m - 1) { r = midMaxValue(x + 1, y); }
      if (y < n - 1) { d = midMaxValue(x, y + 1); }
      dp[key] = grid[x][y] + (r > d ? r : d);
      return dp[key];
    }
  }

  return midMaxValue(0, 0);
};

let grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
];
console.log(maxValue(grid));