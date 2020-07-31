// 面试题 04.03. 特定深度节点链表
// 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

// Definition for a binary tree node.
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

// Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {TreeNode} tree
 * @return {ListNode[]}
 */
var listOfDepth = function(tree) {
  if (!tree) { return []; }
  let res = [[tree]];
  let forward = true;
  while (forward) {
    forward = false;
    let pre = res[res.length - 1];
    let now = [];
    for (let node of pre) {
      if (node.left) { now.push(node.left); }
      if (node.right) { now.push(node.right); }
    }
    if (now.length > 0) {
      res.push(now);
      forward = true;
    }
  }
  res = res.map(nodes => {
    let listnode = new ListNode(nodes[0].val);
    let tmp = listnode;
    for (let i = 1; i < nodes.length; i++) {
      listnode.next = new ListNode(nodes[i].val);
      listnode = listnode.next;
    }
    return tmp;
  })
  return res;
};