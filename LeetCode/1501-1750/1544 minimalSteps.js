// LCP 13. 寻宝
// 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
// 迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
// 要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。
// 迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。
// 我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。
/**
 * @param {string[]} maze
 * @return {number}
 */
var minimalSteps = function(maze) {
  maze = maze.map(str => Array.from(str));
  m = maze.length;
  n = maze[0].length;
  for (let row of maze) { console.log(row); }

  // 利用 bfs 找到 start 到 end 最短路径长度，没有返回 -1
  function findMinSteps(start = {}, end = {}) {
    const legalRow = row => 0 <= row && row < m
    const legalCol = col => 0 <= col && col < n

    let visit = Array(m);
    for (let i = 0; i < m; i++) {
      visit[i] = Array(n).fill(false);
    }
    visit[start.x][start.y] = true;
    // bfs 存储每一层遍历到达的位置，第一层为 start
    let bfs = [[{x: start.x, y: start.y}]]
    // arrive: 是否到达 end
    // forward: 本次 bfs 是否前进
    let arrive = false;
    let forward = true;
    while (!arrive && forward) {
      forward = false;
      bfs[bfs.length] = []
      for (let {x: posX, y: posY} of bfs[bfs.length - 2]) {
        neighbors = [
          {x: posX - 1, y: posY}, {x: posX + 1, y: posY},
          {x: posX, y: posY - 1}, {x: posX, y: posY + 1}
        ]
        for (let {x, y} of neighbors) {
          if (legalRow(x) && legalCol(y) && !visit[x][y] && maze[x][y] !== '#' ) {
            bfs[bfs.length - 1].push({x, y});
            visit[x][y] = true;
            forward = true;
            if (x === end.x && y === end.y) {
              arrive = true;
              break;
            }
          }
        }
        if (arrive) { break; }
      }
    }
    const minLen = arrive ? bfs.length - 1 : -1;
    return minLen;
  }

  let S = null, T = null, Ms = [], Os = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if(maze[i][j] === 'M') { Ms.push({x: i, y: j}); }
      else if(maze[i][j] === 'O') { Os.push({x: i, y: j}); }
      else if(maze[i][j] === 'S') { S = {x: i, y: j}; }
      else if(maze[i][j] === 'T') { T = {x: i, y: j}; }
    }
  }

  if (Ms.length === 0) { return findMinSteps(S, T); }
  else {
    const path = (from = {}, to = {}) => `(${from.x},${from.y}) to (${to.x},${to.y})`;

    let mem = {};
    // 找到 S 到每个 M 的最短路径长度
    for (let M of Ms) {
      for (let O of Os) {
        const minSO = findMinSteps(S, O);
        const minOM = findMinSteps(O, M);
        mem[path(S, M)] = minOM > 0 && minOM > 0 ? minSO + minOM : -1;
        if (mem[path(S, M)] === -1) { return -1; }
      }
    }
    // 找到 M 到每个不同 M 的最短路径长度
    for (let M1 of Ms) {
      for (let M2 of Ms) {
        if (M1 !== M2 && !mem[`(${M1.x},${M1.y}) to (${M2.x},${M2.y})`]) {
          for (let O of Os) {
            const minM1O = findMinSteps(M1, O);
            const minOM2 = findMinSteps(O, M2);
            mem[path(M1, M2)] = minM1O > 0 && minOM2 > 0 ? minM1O + minOM2 : -1;
            mem[path(M2, M1)] = mem[path(M1, M2)];
            if (mem[path(M1, M2)] === -1) { return -1; }
          }
        }
      }
    }
    // 找到每个 M 到 T 的最短路径长度
    for (let M of Ms) {
      const minMT = findMinSteps(M, T);
      mem[path(M, T)] = minMT > 0 ? minMT : -1;
      if (mem[path(M, T)] === -1) { return -1; }
    }

    console.log(mem);
    console.log();

    let dp = {};
    const dpKey = (cur = {}, MState = []) => `(${cur.x},${cur.y}):${MState.join('')}`;
    function dfs(cur = {}, MState = [], steps, nodes = []) {
      if (!MState.includes(0)) {
        console.log(nodes);
        console.log(steps);
        // console.log(dp[dpKey(cur, MState)]);
        console.log();
      }
      if (dp[dpKey(cur, MState)]) { return dp[dpKey(cur, MState)]; }
      else {
        let minLen = Number.MAX_SAFE_INTEGER;
        if (MState.includes(0)) {
          for (let i = 0; i < MState.length; i++) {
            if (MState[i] === 0) {
              // if (nodes.length === 4) {
              //   console.log(nodes);
              //   console.log(MState);
              //   console.log(Ms[i]);
              //   console.log(steps);
              //   console.log(dp);
              //   console.log();
              // }
              let MStateTmp = Object.assign([], MState);
              MStateTmp[i] = 1;
              let minLenTmp = dfs(Ms[i], MStateTmp, steps + mem[path(cur, Ms[i])], [...nodes, cur]) + mem[path(cur, Ms[i])];
              if (minLenTmp < minLen) { minLen = minLenTmp; }
            }
          }
        }
        dp[dpKey(cur, MState)] = minLen !== Number.MAX_SAFE_INTEGER ? minLen : mem[path(cur, T)];
        return dp[dpKey(cur, MState)];
      }
    }
    const minLen = dfs(S, Array(Ms.length).fill(0), 0, []);
    // console.log(dp);
    return minLen;
  }
};

// 16
// let maze = ["S#O", "M..", "M.T"];
// 17
// let maze = ["S#O", "M.T", "M.."]
// -1
// let maze = ["S.#.M","O.#.O","M.#.T"]
// 28
let maze = [".MM..", "#..M.", ".#..#", "..O..", ".S.OM", ".#M#T", "###..", "....."]
// -1
// let maze = ["S.#.M","O.#.O","M.#.T"]
// 60
// let maze = ["......", "M....M", ".M#...", "....M.", "##.TM.", "...O..", ".S##O.", "M#..M.", "#....."]
console.log(minimalSteps(maze));