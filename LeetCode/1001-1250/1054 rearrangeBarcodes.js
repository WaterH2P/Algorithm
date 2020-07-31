// 1054. 距离相等的条形码
// 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
// 请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

/**
 * @param {number[]} barcodes
 * @return {number[]}
 */
var rearrangeBarcodes = function(barcodes = []) {
  if (barcodes.length <= 2) { return barcodes; }
  // 数组排序
  barcodes.sort();

  const len = barcodes.length;
  let mid = Number.parseInt(len / 2);
  let listL = undefined, listR = undefined;
  let l = 0, r = mid;
  // 如果长度为奇数，则 listL 长度加一
  if (len % 2 !== 0) { r = mid + 1; }
  // 窗口滑动
  while (r < barcodes.length && barcodes[r - 1] === barcodes[r]) {
    l += 1;
    r += 1;
  }
  listL = barcodes.slice(l, r);
  listR = [...barcodes.slice(0, l), ...barcodes.slice(r)]

  // 新建一个 array，将 listL 和 listR 数据插入其中
  let res = Array(len);
  for (let i = 0; i < listR.length; i++) {
    res[2 * i] = listL[i];
    res[2 * i + 1] = listR[mid - 1 - i];
  }

  if (len % 2 !== 0) { res[len - 1] = listL[mid]; }
  return res;
};

let barcodes = [7,7,7,8,5,7,5,5,5,8];
console.log(rearrangeBarcodes(barcodes));